import subprocess
import json
import sys
from time import sleep
import os
import asyncio
from kasa import SmartPlug

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

    async def cycle_plug(self):
        try:
            p = SmartPlug(self.settings['WiFiPlugIPAddress'])
            await p.update()
            await p.turn_off()
            sleep(20)
            await p.turn_on()
            sleep(self.fail_timeouts[self.fail_count])
        except Exception as e:
            print(f"Exception: {e}")
            return False
        return True

    def _runner(self):
        while True:
            for i in range(0, 5):
                success = ping()
                if success:
                    break
                else:
                    sleep(3)
            if success:
                print(Fore.GREEN, "Internet is ALIVE!")
                self.fail_count = 0
                sleep(120)
            else:
                print(Fore.RED, "Internet is broken, REBOOTING!")
                self.fail_count += 1
                if self.fail_count > 6:
                    self.fail_count = 6
                asyncio.run(self.cycle_plug())
            sleep(0.1)


wp = WiFiPlug()
wp._runner()