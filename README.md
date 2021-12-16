# wifiplug_internet_maintainer v1.9.1
Polls the internet for alive status and if not cycles a tp-link kasa plug.  
Supports Windows, Linux and MacOS.

You'll need to buy a wifi router if you don't already have one and hardwire it to your internet service provider's router, then connect all your devices to your purchased wifi router.

If internet is down, cycle the power to the router (waiting 20 seconds between off and on states).  
Increases poll times until 2 hours then sticks at 2 hours until recovery.

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
run 'pyinstaller plug.py'

This will create a dist directory in your repo directory. 
Copy the entirety of the plug directory contained within the dist directory (not dist itself) into c:\program files (x86) (you may need to have admin privileges for this operation).

Press windows key + r and type in 'shell:startup' Create a shortcut for the target 'c:\program files (x86)\plug\plug.exe' and put it in the shell:startup directory.

Reboot!

# MacOS setup
If you want to bundle this into an executable, do the following:

Install virtualenv (googleable). 
Clone the repo. 
Navigate to the repo directory. 
run 'virtualenv venv' 
run 'source venv/bin/activate' 
run 'pip install -r requirements.txt' 
run 'pyinstaller plug.py'

This will create a dist\plug directory in your repo directory. 
Rename it to routerplug if you want.  For example, if you have more than one Kasa plug.

In System Preferences, select Users and Groups, then select yourself or admin as a user, unlock, enter your password and press the top right button 'Login items.'
Now with the '+' button, select the plug application in the dist\plug directory.  Relock.

Reboot!

