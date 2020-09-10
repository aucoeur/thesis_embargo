import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

if __name__ == "__main__":
    # Set Scopes for API
    scope = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file'
        ]   

    # File with service account credentials
    file_name = 'sacredentials.json' 

    # store credentials from file with access scopes
    creds = ServiceAccountCredentials.from_json_keyfile_name(file_name, scope)

    # authorize sheets
    client = gspread.authorize(creds)

    # get sheets
    sheet = client.open('Test API Integration').sheet1

    sheet_data = sheet.get_all_records()
    pp = pprint.PrettyPrinter()
    pp.pprint(sheet_data)

