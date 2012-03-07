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
from Products.Zuul.interfaces import IBasicDataSourceInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class IPostgresqlMonitorDataSourceInfo(IBasicDataSourceInfo):
    timeout = schema.Int(title=_t(u'Timeout (seconds)'))
    hostname = schema.Text(title=_t(u'PostgreSQL Host'), group=_t(u'Postgresql'))
    username = schema.Text(title=_t(u'PostgreSQL Username'), group=_t(u'Postgresql'))
    port = schema.Text(title=_t(u'PostgreSQL Port'), group=_t(u'Postgresql'))
    password = schema.Password(title=_t(u'PostgreSQL Password'), group=_t(u'Postgresql'))
    
    
    

