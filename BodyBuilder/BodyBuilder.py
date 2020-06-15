#!/usr/bin/env python3
import configparser
import json
import time
from influxdb import InfluxDBClient

config = configparser.ConfigParser()
config.read('/etc/monigraf/monigraf.ini')
passdb = config['influxdb']['password']
if config['influxdb']['ssl'] == "True": client = InfluxDBClient(host=config['influxdb']['server'], port=8086, username=config['influxdb']['username'], password=passdb, ssl=True, verify_ssl=False)
else: client = InfluxDBClient(host=config['influxdb']['server'], port=8086, username=config['influxdb']['username'], password=passdb)
client.switch_database(config['influxdb']['dbname'])
body = {}
body['tags'] = {}
body['fields'] = {}

class BuildBody():
    def __init__(self, measurement, host):
        body['measurement'] = measurement
        body['tags']['host'] = host

    def add_tag(self, key, value): body['tags'][key] = value
    def del_tag(self, key): del body['tags'][key]
    def add_field(self, key, value): body['fields'][key] = value

    def Add(self):
        client.write_points([body])
        body['fields'] = {}
    def Delete(self): client.delete_series(tags={'host':body['tags']['host']},measurement=body['measurement'])
