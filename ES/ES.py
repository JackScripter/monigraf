#!/usr/bin/env python3
import hashlib
import random
import configparser
from datetime import datetime
from elasticsearch import Elasticsearch

config = configparser.ConfigParser()
config.read('/etc/monigraf/monigraf.ini')

class ES():
    #def __init__(self, host, user, password, ca, index):
    def __init__(self, index):
        self.data = {}
        unprocessed_indexID = str(datetime.utcnow()) + str(random.randrange(1,100,1))
        self.indexID = str(hashlib.sha256(unprocessed_indexID.encode("utf-8")).hexdigest())
      #  cred = user + ':' + str(password)
        self.es = Elasticsearch(
            [config['datasource_elasticsearch']['server']],
            use_ssl=False
      #      ca_certs=ca,
      #      http_auth=cred
	)
        self.index = index + '-' + datetime.now().strftime("%Y.%m.%d")
        try:
            self.es.get(index=self.index, id=self.indexID)['_source']
        except:
            self.es.indices.create(index=self.index, ignore=400)

    def create_list(self, key): self.data[key] = []
    def add_data(self, key, value): self.data[key] = value
    def add_listdata(self, key, value): self.data[key].append(value)

    def send(self):
        self.data['timestamp'] = datetime.utcnow()
        self.es.index(index=self.index, id=self.indexID, body=self.data)
        self.data = {}
