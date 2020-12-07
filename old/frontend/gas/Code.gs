//CREATE CUSTOM MENU
function onOpen() { 
  var ui = SpreadsheetApp.getUi();
  ui.createMenu("Custom Menu")
    .addItem("Sidebar Form","showFormInSidebar")
    .addToUi();
}

//OPEN THE FORM IN SIDEBAR 
function showFormInSidebar() {      
  var form = HtmlService.createTemplateFromFile('Index').evaluate().setTitle('Parse Info');
  SpreadsheetApp.getUi().showSidebar(form);
}

//PARSE DATA
function parse(text) {
  const headers = ["Reason for Requesting Exception: ", "Requestor Name: ", "Requestor Email: ", "Thesis Author: ", "Thesis Title: ", "Graduation Year: ", "Advisor Name: ", "Advisor Email: ", "Division: ", "Exception Type: ", "Request: " ]
  for (let i = 0; i < headers.length; i++) {
    const regex = "[\s\d\w\.]*"
    const reg_data = new RegExp((headers[i]) + (regex) + (headers[i+1]), "gi")
    let result = text.match(reg_data);
    console.log(result);
    return result;
  }
}

//PROCESS FORM
function processForm(formObject){ 
  var sheet = SpreadsheetApp.getActive().getActiveSheet();
  sheet.appendRow([new Date(), formObject.requestor_name, formObject.thesis_title, formObject.request_type, formObject.email, parse(formObject.parse)]);
}

//INCLUDE HTML PARTS, EG. JAVASCRIPT, CSS, OTHER HTML FILES
function include(filename) {
  return HtmlService.createHtmlOutputFromFile(filename).getContent();
}