#!/usr/local/bin/python3.7
import subprocess
#import os
from multiprocessing import Pool

monitor_module = {"smart": "3600", "network": "3600"}
processes = []
def run_process(process):
	#os.system('{}'.format(process))
	subprocess.run(['/bin/bash', process])

#processes = len(monitor_module)		# How many processor will be needed.
#pool = Pool(processes=2)		# How many processor will be needed in the pool.

for x, y in monitor_module.items():
	modpath = "/opt/monigraf/modules/" + x
	processes.append(modpath)

pool = Pool(processes=2)
pool.map(run_process, processes)
