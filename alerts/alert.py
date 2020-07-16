#!/usr/bin/env python3
import configparser
import ast
import importlib

config = configparser.ConfigParser()
config.read('/etc/monigraf/monigraf.ini')

class Alerts():
    def __init__(self, msg):
        for item in ast.literal_eval(config['DEFAULT']['ALERTING_SERVICES']):
            full_module = item + '.' + item
            module = importlib.import_module(full_module)
            module.SendText(msg)
