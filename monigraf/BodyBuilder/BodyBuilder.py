#!/usr/bin/python3.7
import configparser
import json
from influxdb import InfluxDBClient

config = configparser.ConfigParser()
config.read('/etc/monigraf/monigraf.ini')
passdb = config['influxdb']['password']
client = InfluxDBClient(host=config['influxdb']['server'], port=8086, username=config['influxdb']['username'], password=passdb)
client.switch_database(config['influxdb']['dbname'])
body = {}
body['tags'] = {}
body['fields'] = {}

class BuildBody(object):
    def __init__(self, measurement, host):
        body['measurement'] = measurement
        body['tags']['host'] = host

    def add_tag(self, key, value): body['tags'][key] = value
    def add_field(self, key, value): body['fields'][key] = value

    def Send(self):
        data = json.dumps([body])
        client.write_points(data)
