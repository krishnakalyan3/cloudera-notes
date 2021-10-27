#!/usr/bin/env python

from apache_ranger.model.ranger_service import *
from apache_ranger.client.ranger_client import *
from apache_ranger.model.ranger_policy  import *
import json

# Load Json Export
with open('/root/ranger_hdfs_filter.json') as f:
    json_data = json.load(f)

# Just Updated the Config required to be changed
eval_config = eval(json_data['config'])

# Filter for audit rules
ranger_url  = 'http://ranger_host:6080'
ranger_auth = ('admin', 'admin123')
ranger = RangerClient(ranger_url, ranger_auth)
services = ranger.find_services()

retrieved_service = ranger.get_service('cm_hdfs')
retrieved_service['description'] = 'Cloudera PS Update'
retrieved_service['configs']['ranger.plugin.audit.filters']  = eval_config['ranger.plugin.audit.filters']
retrieved_service['configs']['ranger.accesslogs.exclude.users.list'] = eval_config['ranger.accesslogs.exclude.users.list']

updated_service =  ranger.update_service('cm_hdfs', retrieved_service)
