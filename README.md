# Vulcan
Although more recently a Star Treck reference, the roman god of fire was Vulcan, and so that was a fitting name for this project. This is at least version 3 that has been published online. And here we are again, hopefully for the last time.
## Aims
- Gather temperature data from two DS18B20+ probes.
- Upload to a google sheet rather than a local database.
- Run off a Pi Zero W, (low power)
- Ability to generate graphs, whether locally on Google Sheets I don't know
- Sense when we need to update the data, rather than just spamming it
## Google Sheet
After reading (this)[https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html] article, Google Sheets seemed perfect. However I do not want to blindly upload data, there should be some logic involved.
## Getting Started
Follow the above article. To setup access with Google Sheets, then add your `client_secret.json`, which I haven't provided for obvious reasons. Then add `dtoverlay=w1-gpio` to your `/boot/config.txt` and setup a cronjob. Then have fun!
### Thanks
- (RogerW)[https://www.raspberrypi.org/forums/memberlist.php?mode=viewprofile&u=128609&sid=39b432f0e2a77a561a048340c921cd1c] for providing the api to access the probes
