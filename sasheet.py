import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import json
from flask import Flask, request, url_for, redirect
import os

app = Flask(__name__)

class Parser(object):
    #constructor: takes in file name to parse through it    
    def __init__(self, source): 
        self.fields = [              #dictionary for info parsed from  text file
            ['date_time'],
            ['exception_reason'],
            ['requestor_name'],
            ['requestor_email'],
            ['thesis_author'],
            ['thesis_title'],
            ['grad_year'],
            ['advisor_name'],
            ['advisor_email'],  
            ['division'],
            ['type'],
            ['request'],
            ['patent', False]
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
                #get date and time email was sent
                if line.startswith('Submitted on '):
                    #for some reason when you copy paste the email directly to text file, 
                    #Dear <name> moves to the same line as the date and time, the following code removes that
                    temp = line[13:]
                    temp = temp.split()
                    for i in range(len(temp)):
                        if temp[i] == "Dear":
                            self.fields[0].append(" ".join(temp[:i-1]))
                            break
                #for Emargo Reason info
                if line.startswith('Reason for Requesting Exception:'):
                    start =  True       #the first field we fill in should be the embargo reason
                    currField = 1
                    self.removeTitle(line, currField)
                elif start == True:
                    #for Requestor Name's info
                    if line.startswith('Requestor Name: '):
                        currField = 2
                        self.removeTitle(line, currField)
                    #for Requestor Email's info
                    elif line.startswith('Requestor Email: '):
                        currField = 3
                        self.removeTitle(line, currField)
                    #for Thesis Author info
                    elif line.startswith('Thesis Author: '):
                        currField = 4
                        self.removeTitle(line, currField)
                    #for Thesis Title info
                    elif line.startswith('Thesis Title: '):
                        currField = 5
                        self.removeTitle(line, currField)
                    #for Grad Year info
                    elif line.startswith('Graduation Year: '):
                        currField = 6
                        self.removeTitle(line, currField)
                    #for Advisor Name info
                    elif line.startswith('Advisor Name: '):
                        currField = 7
                        self.removeTitle(line, currField)
                    #for Advisor Email info
                    elif line.startswith('Advisor Email: '):
                        currField = 8
                        self.removeTitle(line, currField)
                    #for Division info
                    elif line.startswith('Division: '):
                        currField = 9
                        self.removeTitle(line, currField)
                    #for Exception Type info
                    elif line.startswith('Exception Type: '):
                        currField = 10
                        self.removeTitle(line, currField)
                    #for Request info
                    elif line.startswith('Request: '):
                        currField = 11
                        self.removeTitle(line, currField)
                    #for when the current line doesnt have a title attatched to it, 
                    # assume it's continuing info from the last found field
                    else:
                        self.fields[currField][1] += " " +  line
                        if "Patents pending:" in line:
                            self.fields[12][1] = True


    #converts the fields to a dict
    def to_Dict(self):
        dic = {}
        for item in self.fields:
            dic[item[0]] = item[1]
        
        return dic

class Sheets(object):
    def __init__(self):
        # Set Scopes for API
        self.scope = [
            'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/drive.file'
            ]   
        
        self.file_name = 'sacredentials.json'                                            #File with service account credentials
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(self.file_name, self.scope)  #store credentials from file with access scopes
        self.client = gspread.authorize(self.creds)                                           #authorize sheets
        self.spread = self.client.open('Test API Integration')                                #open the google sheets

#recieves json from front end and then converts it to a text file to be parsed
@app.route('/api/recieve', methods=['GET'])
def recieve():
    data = request.get_json()               #recieves json from frontend
    data = json.load(data)                  #converts json to dictionary
    text = data["text"]                     #dictionary should onyl have 1 filed "text" which habe the copy pasted text
    file = open("sample_submissions/submission.txt", "w")   #open a  new text file
    file.write(text)                                        #write the text from the json dic to text file
    file.close()                                            #close text file
    return redirect(url_for('parsed'))           #after getting the text, redirect to the  parser

#parses a text file and posts results to google sheets
@app.route('/api/parsed')
def parsed():
    sheet = Sheets()

    parsing = sheet.spread.worksheet("ParsedData")                                      #select the ParsedData sheet
    decision = sheet.spread.worksheet("Decisions")                                     #select the ParsedData sheet

    parsed = Parser("sample")      #parses data from txt file

    #updating the ParsedData Sheet
    row = 2
    col = 1
    for item in parsed.fields:
        if parsing.cell(row, col).value == '':
            parsing.update_cell(row, col, item[1])
            col += 1
        else:
            row+=1

    #updating the Decisions Sheet
    row = 2
    while True:
        if parsing.cell(row, col).value == '':
            break
        else:
            row+=1
    parsedDict = parsed.to_Dict()
    for field in parsedDict.keys():
        if field == "thesis_title":
            decision.update_cell(row, 1, parsedDict[field])
        elif field == "thesis_author":
            decision.update_cell(row, 2, parsedDict[field])
        elif field == "advisor_name":
            decision.update_cell(row, 3, parsedDict[field])
        elif field == "date_time":
            decision.update_cell(row, 4, parsedDict[field])
        




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
    
    

    
    




    # # get sheets
    # sheet = client.open('Test API Integration').sheet4
    # sheet_data = sheet.get_all_records()
    # pp = pprint.PrettyPrinter()
    # pp.pprint(sheet_data)
    # sheet.update()
    # 
    # print(parsed.to_Json())

    







    



    