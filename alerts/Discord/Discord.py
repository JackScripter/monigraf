#!/usr/bin/env python3
import requests
import configparser

config = configparser.ConfigParser()
config.read('/etc/monigraf/monigraf.ini')

def SendText(msg):
    webhook = config['Discord']['webhook']
    send = '``' + msg + '``'
    requests.post(webhook, json={'username':config['Discord']['username'], 'content':str(send)}, headers={'Content-Type': 'application/json'})

