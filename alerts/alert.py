#!/usr/bin/env python3
import configparser
import ast
import importlib
import datetime

config = configparser.ConfigParser()
config.read('/etc/monigraf/monigraf.ini')

class Alerts():
    def __init__(self, msg):
        for item in ast.literal_eval(config['DEFAULT']['ALERTING_SERVICES']):
            full_module = item + '.' + item
            module = importlib.import_module(full_module)
            now = str(datetime.datetime.fromtimestamp(datetime.datetime.timestamp(datetime.datetime.now())))
            msg = str('`[' + now + '] ' + msg + '`')
            module.SendText(msg)
