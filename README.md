# wifiplug_internet_maintainer
Polls the internet for alive status and if not cycles a tp-link kasa plug

If internet is down, cycle the power to the router (waiting 20 seconds between off and on statuses).  
Increases poll times until 2 hours then sticks at 2 hours until recovery.
