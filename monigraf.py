#!/usr/bin/python3.7
import subprocess
import configparser
import ast
from multiprocessing import Pool

# Config file location
config = configparser.ConfigParser()
config.read('/etc/monigraf/monigraf.ini')

processes = []

def run_process(process):
    subprocess.run([process, 'check'])

for x in ast.literal_eval(config['DEFAULT']['MOD_ENABLED']):
    modpath = config['DEFAULT']['MOD_PATH'] + x
    processes.append(modpath)

pool = Pool(processes=len(processes))
pool.map(run_process, processes)
