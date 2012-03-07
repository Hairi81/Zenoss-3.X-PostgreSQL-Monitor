###########################################################################
#
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
#
###########################################################################

import Globals
import os.path

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
from Products.CMFCore.DirectoryView import registerDirectory
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

from Products.ZenModel.ZenPack import ZenPackBase

class ZenPack(ZenPackBase):
    """ Postgresql loader
    """

    packZProperties = [
            ('zPostgresqlUsername', 'postgres', 'string'),
            ('zPostgresqlPassword', 'postgres', 'string'),
	    ('zPostgresqlDatabase', 'postgres', 'string'),
            ]

    def install(self, app):
        ZenPackBase.install(self, app)
        self.enableDefaultProcessMonitoring(app.zport.dmd)

    def upgrade(self, app):
        ZenPackBase.upgrade(self, app)
        self.enableDefaultProcessMonitoring(app.zport.dmd)

    def enableDefaultProcessMonitoring(self, dmd):
        try:
            p = dmd.Processes.PostgreSQL.osProcessClasses.postgre
            if p.hasProperty('zMonitor'): return
            log.info('Enabling monitoring for postgres processes.')
            p._setProperty('zMonitor', True)
            for i in p.instances():
                i.index_object()
        except AttributeError:
            pass
