from flask import Flask, request, url_for, redirect
import os
from sasheet import Parser, Sheets
import json

app = Flask(__name__)

#recieves json from front end and then converts it to a text file to be parsed
@app.route('/api/recieve', methods=['GET'])
def recieve():
    data = request.get_json()                               #recieves json from frontend
    data = json.loads(data)                                 #converts json to dictionary
    text = data["text"]                                     #dictionary should only have 1 filed "text" which habe the copy pasted text
    file = open("sample_submissions/submission.txt", "w")   #open a new text file
    file.write(text)                                        #write the text from the json dic to text file
    file.close()                                            #close text file

    #update the latter half of the decions sheet
    sheet = Sheets()
    decision = sheet.spread.worksheet("Decisions")          #select the Decisions sheet
    row = 2
    while True:
        if decision.cell(row, 1).value == '':
            break
        else:
            row+=1
    decision.update_cell(row, 5, data["decisions"])
    decision.update_cell(row, 6, data["comments"])
    decision.update_cell(row, 7, data["signature"])


    return redirect(url_for('parsed'))                      #after getting the text, redirect to the parser

#parses a text file and posts results to google sheets
@app.route('/api/parsed')
def parsed():
    sheet = Sheets()
    parsing = sheet.spread.worksheet("ParsedData")                                     #select the ParsedData sheet
    decision = sheet.spread.worksheet("Decisions")                                     #select the Decisions sheet

    parsed = Parser("sample")      #parses data from txt file

    #updating the ParsedData Sheet
    row = 2
    col = 1
    for item in parsed.fields:
        if parsing.cell(row, 1).value == '':
            parsing.update_cell(row, col, item[1])
            col += 1
        else:
            row+=1

    #updating the Decisions Sheet
    row = 2
    while True:
        if decision.cell(row, 1).value == '':
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
