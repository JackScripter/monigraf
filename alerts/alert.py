#!/usr/bin/env python3
import configparser

config = configparser.ConfigParser()
config.read('/etc/monigraf/monigraf.ini')

def GetEnabledAlerts():
    return config['DEFAULT']['ALERTING_SERVICES']
