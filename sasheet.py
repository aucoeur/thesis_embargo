import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

class Parser(object):
    def __init__(self, source): 
        self.fields = {               #dictionary for info parsed from  text file
            'embargo_reason': '',
            'requestor_name': '',
            'requestor_email': '',
            'thesis_author': '',
            'thesis_title': '',
            'grad_year': '',
            'advisor_name': '',
            'advisor_email':'',
            'division':'',
            'type': '',
            'request': '',
            'patent': False
        }
        self.parse(source)

    #removes the field's name from the line and then adds the info to the appropriate field in the dic
    def removeTitle(self, line, currField):
        for i in range(len(line)):
            if line[i] == ':':
                self.fields[currField] += line[i+1:len(line)]
        return "FAILED TO REMOVE TITLE"

    def parse(self, source):
        currField = ''      #keep track of which field we're adding to
        start = False       #keep track of if we've started to run into the info we want now
        #opens text file
        with open(f'{source}.txt', 'r') as text:
            #loops through every line in the text file
            for line in text:
                line = line.strip()        #strips /n marks
                line = line.strip()        #strips trailing and beginnign white spaces
                #for Emargo Reason info
                if line.startswith('Reason for Requesting Exception:'):
                    start =  True       #the first field we fill in should be the embargo reason
                    currField = 'embargo_reason'
                    self.removeTitle(line, currField)
                if start == True:
                    #for Requestor Name's info
                    if line.startswith('Requestor Name: '):
                        currField = 'requestor_name'
                        self.removeTitle(line, currField)
                    #for Requestor Email's info
                    elif line.startswith('Requestor Email: '):
                        currField = 'requestor_email'
                        self.removeTitle(line, currField)
                    #for Thesis Author info
                    elif line.startswith('Thesis Author: '):
                        currField = 'thesis_author'
                    #for Thesis Title info
                    elif line.startswith('Thesis Title: '):
                        currField = 'thesis_title'
                        self.removeTitle(line, currField)
                    #for Grad Year info
                    elif line.startswith('Graduation Year: '):
                        currField = 'grad_year'
                        self.removeTitle(line, currField)
                    #for Advisor Name info
                    elif line.startswith('Advisor Name: '):
                        currField = 'advisor_name'
                        self.removeTitle(line, currField)
                    #for Advisor Email info
                    elif line.startswith('Advisor Email: '):
                        currField = 'advisor_email'
                        self.removeTitle(line, currField)
                    #for Division info
                    elif line.startswith('Division: '):
                        currField = 'division'
                        self.removeTitle(line, currField)
                    #for Exception Type info
                    elif line.startswith('Exception Type: '):
                        currField = 'type'
                        self.removeTitle(line, currField)
                    #for Request info
                    elif line.startswith('Request: '):
                        currField = 'request'
                        self.removeTitle(line, currField)
                    #for when the current line doesnt have a title attatched to it, 
                    # assume its continuing info from the last found field
                    # ONLY if we've started encountering the 
                    else:         
                        self.fields[currField] += line
                        if "Patents pending:" in line:
                            self.fields['patent'] = True

    #converts the field's dic to JSON
    def to_Json(self):
        pass




if __name__ == "__main__":
    # # Set Scopes for API
    # scope = [
    #     'https://www.googleapis.com/auth/drive',
    #     'https://www.googleapis.com/auth/drive.file'
    #     ]   

    # # File with service account credentials
    # file_name = 'sacredentials.json' 

    # # store credentials from file with access scopes
    # creds = ServiceAccountCredentials.from_json_keyfile_name(file_name, scope)

    # # authorize sheets
    # client = gspread.authorize(creds)

    # # get sheets
    # sheet = client.open('Test API Integration').sheet1

    # sheet_data = sheet.get_all_records()
    # pp = pprint.PrettyPrinter()
    # pp.pprint(sheet_data)


    # sheet.update()


    parsed = Parser("sample1")
    print(parsed.fields)



    