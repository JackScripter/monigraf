#!/usr/bin/env python3
import requests
import configparser

config = configparser.ConfigParser()
config.read('/etc/monigraf/monigraf.ini')

def SendText(msg):
    token = config['Telegram']['token']
    chat_id = config['Telegram']['chat_id']
    send = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + msg
    response = requests.get(send)

