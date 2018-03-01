import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1FEaaJdhnomaV2fPBwO0fLfqNK6_bnncfy7SIWvOPZFQ/edit?usp=drive_web&ouid=103704144020418407446").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)