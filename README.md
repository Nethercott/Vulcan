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
