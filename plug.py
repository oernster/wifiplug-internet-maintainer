import subprocess
from time import sleep

import os

from colorama import init, Fore


init()

def ping():    
    hostname = "google.com"
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        return True
    else:
        return False


class WiFiPlug(object):
    def __init__(self):
        self.IPAddress = '10.0.0.17'
        self.fail_timeouts = {
            1: 300, # 5 mins
            2: 600, # 10 mins
            3: 900, # 15 mins
            4: 1800, # 30 mins
            5: 3600, # 1 hour
            6: 7200, # 2 hours
        }
        self.fail_count = 0
        
    def off(self):
        args = ['kasa', '--host', self.IPAddress, '--plug', 'off',]
        subprocess.call(args) 

    def on(self):
        args = ['kasa', '--host', self.IPAddress, '--plug', 'on',]
        subprocess.call(args) 

    def cycle_plug(self):
        self.off()
        sleep(20)
        self.on()
        sleep(self.fail_timeouts[self.fail_count])

    def _runner(self):
        while True:
            success = ping()
            if success:
                print(Fore.GREEN, "Internet is ALIVE!")
                self.fail_count = 0
                sleep(120)
            else:
                print(Fore.RED, "Internet is broken, REBOOTING!")
                self.fail_count += 1
                if self.fail_count > 6:
                    self.fail_count = 6
                self.cycle_plug()
            sleep(0.1)


wp = WiFiPlug()
wp._runner()