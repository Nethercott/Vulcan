from ds18b20 import DS18B20
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Vulcan").sheet1
row_count = sheet.row_count
# DS18B20
probes = DS18B20()
probe_count = probes.device_count()

"""
So the old temperature is 18C and the new temperature is 21C, offset is 2, this would return true, and so should now post into the Google Sheet.
"""
def rangeCheck(old_number, offset, new_number): # Thanks @Eladkay, for this
    return not new_number <= (old_number + offset) and new_number > (old_number - offset)

"""
Get the last temperatures posting, compare to the current temperatures. If they exceed offsets, send an update to the google sheet
"""
def main():



if __name__ == '__main__':
    main()
