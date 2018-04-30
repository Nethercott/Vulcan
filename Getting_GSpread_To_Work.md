# Getting GSpread to Work
After reading [twilio](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html) article, and then trying to get it to work for almost an hour, there are a couple of things that need to be changed in order to get it too work.
- The `scope` has been changed to `scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']`
- You must also authorise the `Google Sheets API` to have any access to the spreadsheet 
