import getLastRowInCol from './helpers';

function populateCommitee() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Internal');
  const colCheck = sheet.getRange('B:B').getValues();
  const lastRow = getLastRowInCol(colCheck);
  const commitee = sheet.getRange(`B6:B${lastRow}`).getValues();
  return commitee;
}

export default populateCommitee;
