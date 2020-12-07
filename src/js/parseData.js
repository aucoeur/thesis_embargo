const parseData = (text) => {
  const sheet = SpreadsheetApp.getActive().getActiveSheet();
  // console.log(typeof text, text);

  // clean up text formatting since copy/pasting strings might have newline variations
  const cleanText = text.replace(/[\r\n]+/gm, '');
  const dataRow = [new Date()];

  const headers = [
    'Reason for Requesting Exception: ',
    'Requestor Name: ',
    'Requestor Email: ',
    'Thesis Author: ',
    'Thesis Title: ',
    'Graduation Year: ',
    'Advisor Name: ',
    'Advisor Email: ',
    'Division: ',
    'Exception Type: ',
    'Request: ',
  ];

  for (let i = 0; i < headers.length - 1; i += 1) {
    const data = '(.*)';
    const splitData = new RegExp(headers[i] + data + headers[i + 1], 'i');
    const result = cleanText.split(splitData)[1];
    // console.log(typeof result, result);
    dataRow.push(result);
  }

  // Janky way to add the last line (checkbox, same for all requests)
  dataRow.push(
    'Consistent with the Caltech Doctoral Thesis Dissemination policy, I am requesting an exception to the 6-month embargo to campus for my PhD thesis.'
  );
  // console.log(typeof dataRow);
  // console.log(dataRow);

  sheet.appendRow(dataRow);
  Logger.log(dataRow);
  return `Request for ${dataRow[4]} parsed and added to sheet`;
};

// parseData(testString);

export default parseData;
