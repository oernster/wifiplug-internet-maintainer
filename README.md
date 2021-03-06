# wifiplug_internet_maintainer v1.9.1
Pings google.com every 2 minutes to check for internet alive status.  
If it's dead after 5 pings, the program power cycles a tp-link kasa plug with a break of 20 seconds between off and on states of the WiFi plug.

Supports Windows, Linux and MacOS.

You'll need to buy a wifi router if you don't already have one and hardwire it to your internet service provider's router, then connect all your devices to your purchased wifi router.

Increases poll times starting at 5 minutes incrementally until it reaches 2 hours, then sticks at 2 hours until recovery.

Download the Kasa app from your App Store for your mobile.  Define the name of the router plug exactly as 'Router Wifi plug'

# Supported Kasa plugs from TP-Link
HS100
HS103
HS105
HS107
HS110
KP105
KP115
KP401

# Windows setup
If you want to bundle this into an executable, do the following:

Firstly install Python 3 from python.org. I used Python 3.9.7 but I strongly suspect earlier versions as long as they are at least a fairly recent version of Python 3 would be fine. 

Install virtualenv (googleable). 
Clone the repo. 
Navigate to the repo directory. 
run 'virtualenv venv' 
run 'venv\Scripts\activate' 
run 'pip install -r requirements.txt' 
run 'pyinstaller -F plug.py'

This will create a dist directory in your repo directory. 
Create a directory and copy the plug.exe program into c:\program files (x86)\routerplug (you may need to have admin privileges for this operation).

Press windows key + r and type in 'shell:startup' Create a shortcut for the target 'c:\program files (x86)\routerplug\plug.exe' and put it in the shell:startup directory.

Reboot!

# MacOS setup
If you want to bundle this into an executable, do the following:

Install virtualenv (googleable). 
Clone the repo. 
Navigate to the repo directory. 
run 'virtualenv venv' 
run 'source venv/bin/activate' 
run 'pip install -r requirements.txt' 
run 'pyinstaller -F plug.py'

This will create a dist directory in your repo directory. 
Rename the plug executable in the folder to 'routerplug'

Copy the routerplug program to your applications folder on your Mac.

In System Preferences, select Users and Groups, then select yourself or admin as a user, unlock, enter your password and press the top right button 'Login items.'
Now with the '+' button, select the routerplug application.  Relock.

Reboot!

