#!/usr/bin/python3.7
import subprocess
import configparser
from multiprocessing import Pool

# Config file location
config = configparser.ConfigParser()
config.read('/etc/monigraf/monigraf.ini')

monitor_module = ["network"]
processes = []

def run_process(process):
    subprocess.run([process])

#processes = len(monitor_module)	
#pool = Pool(processes=2)

for x in monitor_module:
    modpath = config['DEFAULT']['MOD_PATH'] + x
    processes.append(modpath)

pool = Pool(processes=3)
pool.map(run_process, processes)
