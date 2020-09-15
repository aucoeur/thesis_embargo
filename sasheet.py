import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

class Parser(object):
    def __init(fileName):
        info = {
            'embargo_reason': '',
            'requestor_name': '',
            'requestor_email': '',
            'thesis_author': '',
            'thesis_title': '',
            'grad_year': '',
            'advisor_name': '',
            'advisor_email': '',
            'division': '',
            'request': ''
        }

    def parse(name):
        start = False
        with open(f'{source_text}.txt', 'r') as text:
            for line in text:
                line.strip()
                if line.startswith('Reason for Requesting Embargo:'):
                    bigline = line
                    line = next(lines)
                    while ':' not in line:
                        bigline = bigline + line
                        line = next(lines)
                    info['embargo_reason'] = get_value('Reason for Requesting Embargo:', bigline, '')
                if line.startswith('Reason for Requesting Embargo:'):
                    bigline = line
                    line = next(lines)
                    while ':' not in line:
                        bigline = bigline + line
                        line = next(lines)
                    info['embargo_reason'] = get_value('Reason for Requesting Embargo:', bigline, '')
                if line.startswith('Reason for Requesting Exception:'):
                    bigline = line
                    line = next(lines)
                    while ':' not in line[0:20]:
                        bigline = bigline + line
                        line = next(lines)
                    info['embargo_reason'] = get_value('Reason for Requesting Exception:', bigline, '')
                if line.startswith('<p>Reason for Requesting Exception:'):
                    bigline = line
                    line = next(lines)
                    while ':' not in line:
                        bigline = bigline + line
                        line = next(lines)
                    info['embargo_reason'] = get_value('Reason for Requesting Exception:', bigline, '')
                if line.startswith('Requestor Name: '):
                    info['requestor_name'] = get_value('Requestor Name: ', line, '')
                if line.startswith('Requestor Email: '):
                    info['requestor_email'] = get_value('Requestor Email: ', line, '')
                if line.startswith('Thesis Author: '):
                    info['thesis_author'] = get_value('Thesis Author: ', line, '')
                if line.startswith('Thesis Title: '):
                    info['thesis_title'] = get_value('Thesis Title: ', line, '')
                if line.startswith('Graduation Year: '):
                    info['grad_year'] = get_value('Graduation Year: ', line, None)
                if line.startswith('Advisor Name: '):
                    info['advisor_name'] = get_value('Advisor Name: ', line, '')
                if line.startswith('Advisor Email: '):
                    info['advisor_email'] = get_value('Advisor Email: ', line, '')
                if line.startswith('Division: '):
                    info['division'] = get_value('Division: ', line, '')
                if line.startswith('Request: '):
                    info['request'] = get_value('Request: ', line, '')



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


    sheet.update()



    