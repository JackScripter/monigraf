#!/usr/bin/python3.7
import configparser
import json
import time
from influxdb import InfluxDBClient

config = configparser.ConfigParser()
config.read('/etc/monigraf/monigraf.ini')
passdb = config['influxdb']['password']
client = InfluxDBClient(host=config['influxdb']['server'], port=8086, username=config['influxdb']['username'], password=passdb)
client.switch_database(config['influxdb']['dbname'])
body = {}
body['tags'] = {}
body['fields'] = {}

class BuildBody():
    def __init__(self, measurement, host):
        body['measurement'] = measurement
        body['tags']['host'] = host

    def add_tag(self, key, value): body['tags'][key] = value
    def add_field(self, key, value): body['fields'][key] = value

    def Add(self): client.write_points([body])
    def Delete(self): client.delete_series(tags={'host':body['tags']['host']},measurement=body['measurement'])
