#!/usr/bin/env python3
import socket
import subprocess
import re

class SNMP():
    def __init__(self, community, host):
        self.snmpCommunity = community
        try: self.snmpHost = socket.inet_aton(str(host.decode('utf-8')))
        except: self.snmpHost = socket.gethostbyname(str(host))

    def get(self, oid):
        result = subprocess.run(['/usr/bin/snmpwalk', '-v2c', '-t5', '-r3', '-c', self.snmpCommunity, self.snmpHost, oid, '-Pe', '-On'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        result = re.sub(str(oid), '', result)       # Remove parents OID to keep only child.
        result = re.sub('[a-zA-Z]*[0-9]*:', '', result).replace(' ', '')
        return result
