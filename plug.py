import subprocess
import json
import sys
from time import sleep
import os
import asyncio
import platform

from kasa import SmartPlug, Discover
from colorama import init, Fore


init()

def ping():
    ping_success = False
    system = platform.system()
    if system == "Windows":
        try:
            ping_success = not os.system('ping %s -n 1' % ('google.com',))
        except Exception as e:
            print(f"Exception trying to ping: {ping_success}")
            return ping()
    elif system == "Linux" or system == "Darwin":
        try:
            ping_success = not os.system("ping -c 1 " + "google.com")
        except Exception as e:
            print(f"Exception trying to ping: {ping_success}")
            return ping()
    return ping_success


class WiFiPlug(object):
    def __init__(self):
        self.addresses = []
        self.fail_timeouts = {
            1: 300, # 5 mins
            2: 600, # 10 mins
            3: 900, # 15 mins
            4: 1800, # 30 mins
            5: 3600, # 1 hour
            6: 7200, # 2 hours
        }
        self.fail_count = 0
        asyncio.run(self.initialise())
        self._runner()
        
    async def initialise(self):
        found_devices = await Discover.discover()
        print(found_devices)
        for k in found_devices.keys():
            self.addresses.append(k)

    async def cycle_plug(self):
        try:
            for addr in self.addresses:
                p = SmartPlug(addr)
                await p.update()
                if p.alias == 'Router WiFi plug':
                    await p.turn_off()
                    print(Fore.YELLOW, "Turned Router WiFi plug OFF.")
                    sleep(20)
                    await p.turn_on()
                    print(Fore.YELLOW, "Turned Router WiFi plug ON.")
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