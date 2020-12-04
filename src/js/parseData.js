const parseData = (text) => {
  const sheet = SpreadsheetApp.getActive().getActiveSheet();
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
    const result = text.split(splitData)[1];
    dataRow.push(result);
  }
  sheet.appendRow(dataRow);
  //   console.log(dataRow);
};

// parseData(testString, heads);

export default parseData;
