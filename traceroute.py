import subprocess
import Queue
import re
import os
import pandas as pd
import threading
from time import sleep

ports = pd.read_csv("~/ip_address_table")
ip_addresses = ports['ip_address']
test = ip_addresses[:100]

addresses = test.to_csv(r'~/output.txt', header=None, index=None, sep=' ', mode='a')
os.chdir(r'~/')
open_host = open('output.txt', 'r')
write_results = open('output.txt','a')

ips = []
for i in range(0,100):
    ip = open_host.readline()
    ip_ref = ip.strip()
    ips.append(ip_ref)

class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None
    def run(self, timeout):
        def target():
            print 'Thread started'
            self.process = subprocess.Popen(self.cmd, shell=True)
            self.process.communicate()
            print 'Thread finished'
        thread = threading.Thread(target=target)
        thread.start()
        thread.join(timeout)
        if thread.is_alive():
            print 'thread alive?', thread.is_alive()
            sleep(0.001)
            print 'and now?', thread.is_alive()
            print 'Terminating process'
            self.process.terminate()
            thread.join()
            print command 

for j in range(0,len(ips)):
    command = Command("traceroute %s" % ips[j])
    command.run(timeout=3)

open_host.close()
write_results.close() 

