# PYTHON FILE FOR FORM 2:
# NOT COMPLETED/SUBJECT TO CHANGE

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import json

class Parser(object):
    #constructor: takes in file name to parse through it    
    def __init__(self, source): 
        self.fields = [              #dictionary for info parsed from  text file
            ['university_librarian'],
            ['initials'],
            ['date_of_decision': 'dd/mm/yyyy'],
            ['approval_status': 'y/n'],
            ['comments'],

            ['director_for_innovation'],
            ['initials'],
            ['date_of_decision': 'dd/mm/yyyy'],
            ['approval_status': 'y/n'],
            ['comments'],
            
            ['division_chair'],
            ['initials'],
            ['date_of_decision': 'dd/mm/yyyy'],
            ['approval_status': 'y/n'],
            ['comments'],

            ['dean_of_graduate_studies'],
            ['initials'],
            ['date_of_decision': 'dd/mm/yyyy'],
            ['approval_status': 'y/n'],
            ['comments'],

            ['vice_provost'],
            ['initials'],
            ['date_of_decision': 'dd/mm/yyyy'],
            ['approval_status': 'y/n'],
            ['comments'],

            ['approval_status': 'y/n'],
            ['initials'],
            ['date_added_to_spreadsheet': 'dd/mm/yyyy']
        ]
        self.parse(source)

    #removes the field's name from the line and then adds the info to the appropriate field in the dic
    def removeTitle(self, line, fieldNum):
        for i in range(len(line)):
            if line[i] == ':':
                self.fields[fieldNum].append(line[i+2:len(line)])
        return "FAILED TO REMOVE TITLE"
    
    #parse through text document containing the info and put it into fields
    def parse(self, source):
        currField = 0      #keep track of which field we're adding to
        start = False       #keep track of if we've started to run into the info we want now
        #opens text file
        with open(f'sample_submissions/{source}.txt', 'r') as text:
            #loops through every line in the text file
            for line in text:
                line = line.strip()        #strips trailing and beginnign white spaces
                # #signature
                # if line.startswith('signature '):
                #     #for some reason when you copy paste the email directly to text file, 
                #     #Dear <name> moves to the same line as the date and time, the following code removes that
                #     temp = line[13:]
                #     temp = temp.split()
                #     for i in range(len(temp)):
                #         if temp[i] == "Dear":
                #             self.fields[0].append(" ".join(temp[:i-1]))
                #             break

                #for name of university librarian
                if line.startswith('university_librarian'):
                    start =  True
                    currField = 1
                    self.removeTitle(line, currField)
                if start == True:
                    #for initials
                    if line.startswith('initials'):
                        currField = 2
                        self.removeTitle(line, currField)
                    #for date of decision
                    elif line.startswith(['date_of_decision': 'dd/mm/yyyy']):
                        currField = 3
                        self.removeTitle(line, currField)
                    #for approval status
                    elif line.startswith('approval_status': 'y/n'):
                        currField = 4
                        self.removeTitle(line, currField)
                    #for comment
                    elif line.startswith('comment'):
                        currField = 5
                        self.removeTitle(line, currField)

                #for name of director of innovation
                if line.startswith('director_for_innovation'):
                    start =  True
                    currField = 6
                    self.removeTitle(line, currField)
                if start == True:
                    #for initials
                    if line.startswith('initials'):
                        currField = 7
                        self.removeTitle(line, currField)
                    #for date of decision
                    elif line.startswith(['date_of_decision': 'dd/mm/yyyy']):
                        currField = 8
                        self.removeTitle(line, currField)
                    #for approval status
                    elif line.startswith('approval_status': 'y/n'):
                        currField = 9
                        self.removeTitle(line, currField)
                    #for comment
                    elif line.startswith('comment'):
                        currField = 10
                        self.removeTitle(line, currField)

                #for name of division chair
                if line.startswith('division_chair'):
                    start =  True
                    currField = 11
                    self.removeTitle(line, currField)
                if start == True:
                    #for initials
                    if line.startswith('initials'):
                        currField = 12
                        self.removeTitle(line, currField)
                    #for date of decision
                    elif line.startswith(['date_of_decision': 'dd/mm/yyyy']):
                        currField = 13
                        self.removeTitle(line, currField)
                    #for approval status
                    elif line.startswith('approval_status': 'y/n'):
                        currField = 14
                        self.removeTitle(line, currField)
                    #for comment
                    elif line.startswith('comment'):
                        currField = 15
                        self.removeTitle(line, currField)
                
                #for name of dean of graduate studies
                if line.startswith('dean_of_graduate_studies'):
                    start =  True
                    currField = 16
                    self.removeTitle(line, currField)
                if start == True:
                    #for initials
                    if line.startswith('initials'):
                        currField = 17
                        self.removeTitle(line, currField)
                    #for date of decision
                    elif line.startswith(['date_of_decision': 'dd/mm/yyyy']):
                        currField = 18
                        self.removeTitle(line, currField)
                    #for approval status
                    elif line.startswith('approval_status': 'y/n'):
                        currField = 19
                        self.removeTitle(line, currField)
                    #for comment
                    elif line.startswith('comment'):
                        currField = 20
                        self.removeTitle(line, currField)

                #for name of provost
                if line.startswith('vice_provost'):
                    start =  True
                    currField = 21
                    self.removeTitle(line, currField)
                if start == True:
                    #for initials
                    if line.startswith('initials'):
                        currField = 22
                        self.removeTitle(line, currField)
                    #for date of decision
                    elif line.startswith(['date_of_decision': 'dd/mm/yyyy']):
                        currField = 23
                        self.removeTitle(line, currField)

    #converts the field's dic to JSON
    def to_Json(self):
        dic = {}
        for item in self.fields:
            dic[item[0]] = item[1]
        
        return json.dumps(dic)



if __name__ == "__main__":
    # Set Scopes for API
    scope = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file'
        ]   

    
    file_name = 'sacredentials.json'                                            #File with service account credentials
    creds = ServiceAccountCredentials.from_json_keyfile_name(file_name, scope)  #store credentials from file with access scopes
    client = gspread.authorize(creds)                                           #authorize sheets
    spread = client.open('Test API Integration')                                #open the google sheets
    sheet = spread.worksheet("ParsedData")                                      #select the ParsedData  sheet

    parsed = Parser("sample1")      #parses data from txt file

    
    row = 2
    col = 1
    for item in parsed.fields:
        if sheet.cell(row, col).value == '':
            sheet.update_cell(row, col, item[1])
            col += 1
        else:
            row+=1




    # # get sheets
    # sheet = client.open('Test API Integration').sheet4
    # sheet_data = sheet.get_all_records()
    # pp = pprint.PrettyPrinter()
    # pp.pprint(sheet_data)
    # sheet.update()
    # 
    # print(parsed.to_Json())