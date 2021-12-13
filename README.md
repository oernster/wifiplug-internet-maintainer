# wifiplug_internet_maintainer v1.2.0
Polls the internet for alive status and if not cycles a tp-link kasa plug

If internet is down, cycle the power to the router (waiting 20 seconds between off and on statuses).  
Increases poll times until 2 hours then sticks at 2 hours until recovery.

The IP address for the WiFi plug needs to be defined.  This is set in settings.json.  Settings.json must be located in the same directory as the main program.

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

Firstly install Python 3 from python.org. I used Python 3.9.7 but I strongly suspect earlier versions as long as they are at least a fairly recent version of Python 3 would be fine. Install virtualenv (googleable). Clone the repo. Navigate to the repo directory. run 'virtualenv venv' run 'venv\Scripts\activate' run 'pip install -r requirements.txt' run 'pyinstaller plug.py'

This will create a dist directory in your repo directory. Copy the settings.json file into the '\dist\plug' directory. Copy the entirety of the plug directory contained within the dist directory (not dist itself) into c:\program files (x86) (you may need to have admin priviledges for this operation).

Press windows key + r and type in 'shell:startup' Insert all programs not already integrated into windows 11's personalisation control panel settings that you want as shortcuts. Create a shortcut for the target 'c:\program files (x86)\plug\plug.exe' and put it in the shell:startup directory.

Reboot!
