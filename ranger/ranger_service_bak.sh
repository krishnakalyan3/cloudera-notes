#!/usr/bin/env bash

# Install necessary packages
yum install -y jq

# Ranger Admin URL
export ENDPOINT_RANGER="http://ranger_host:6080"
curl -k -X GET -H "Accept: application/json" -u 'admin:admin'  $ENDPOINT_RANGER/service/public/api/repository | jq . > ranger_filter_bak.json
