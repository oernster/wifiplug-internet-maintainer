import subprocess
import json
import sys
from time import sleep

import os

from colorama import init, Fore


init()

def ping():
    ping_success = False
    try:
        ping_success = not os.system('ping %s -n 1' % ('google.com',))
    except Exception as e:
        print(f"Exception trying to ping: {ping_success}")
        return ping()
    return ping_success


class WiFiPlug(object):
    def __init__(self):
        self.fail_timeouts = {
            1: 300, # 5 mins
            2: 600, # 10 mins
            3: 900, # 15 mins
            4: 1800, # 30 mins
            5: 3600, # 1 hour
            6: 7200, # 2 hours
        }
        self.fail_count = 0
        self.load_settings()
        
    def load_settings(self):
        try:
            with open('settings.json', 'r') as f:
                self.settings = json.loads(f.read())
        except:
            print(Fore.RED, "settings.json file not found!")
            sys.exit()

    def off(self):
        args = ['kasa', '--host', self.settings['WiFiPlugIPAddress'], '--plug', 'off',]
        subprocess.call(args) 

    def on(self):
        args = ['kasa', '--host', self.settings['WiFiPlugIPAddress'], '--plug', 'on',]
        subprocess.call(args) 

    def cycle_plug(self):
        try:
            self.off()
            sleep(20)
            self.on()
            sleep(self.fail_timeouts[self.fail_count])
        except Exception as e:
            print(f"Exception: {e}")
            self.cycle_plug()

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