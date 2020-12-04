const testString = `Submitted values are:
Reason for Requesting Exception: Chapter 2 contains unpublished theory work which is intended for publication in APS
Physical Review B. This also has not been drafted as a paper yet because I have been writing my thesis. This work is
theory, which builds on existing numerical work performed by one of our competitors. As such, there is a high risk of getting
scooped if our work is circulated before we submit.
Requestor Name: Jocelyn Yamasaki
Requestor Email: jocelyny@library.caltech.edu
Thesis Author: Jocelyn Yamasaki
Thesis Title: SAMPLE - Modeling and Development of Superconducting Nanowire Single-Photon Detectors
Graduation Year: 2020
Advisor Name: Keith Schwab
Advisor Email: schwab@caltech.edu
Division: Engineering and Applied Science (EAS)
Exception Type: Extend Embargo for an Additional 6 Months
Request: Consistent with the Caltech Doctoral Thesis Dissemination policy, I am requesting an exception to the 6-month
embargo to campus for my PhD thesis.`;

const parseData = (text) => {
  const sheet = SpreadsheetApp.getActive().getActiveSheet();
  // console.log(typeof text, text);
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

  // console.log(typeof dataRow);
  // console.log(dataRow);

  sheet.appendRow(dataRow);
  Logger.log(dataRow);
  return `Entry ${dataRow[5]} parsed and added to sheet`;
};

// parseData(testString);

export default parseData;
