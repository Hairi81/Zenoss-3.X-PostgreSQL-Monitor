###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010, Zenoss Inc.
# Copyright (C) 2012, Hairi.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################
from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.template import BasicDataSourceInfo
from ZenPacks.Hairi.PostgreSQLMonitor.interfaces import IPostgresqlMonitorDataSourceInfo


class PostgresqlMonitorDataSourceInfo(BasicDataSourceInfo):
    implements(IPostgresqlMonitorDataSourceInfo)
    timeout = ProxyProperty('timeout')
    hostname = ProxyProperty('hostname')
    port = ProxyProperty('port')
    username = ProxyProperty('username')
    password = ProxyProperty('password')
        
    @property
    def testable(self):
        """
        We can NOT test this datsource against a specific device
        """
        return False
    


