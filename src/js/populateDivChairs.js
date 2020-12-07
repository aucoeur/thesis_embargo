import getLastRowInCol from './helpers';

function populateDivChairs() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Internal');
  const colCheck = sheet.getRange('F:F').getValues();
  const lastRow = getLastRowInCol(colCheck);
  const commitee = sheet.getRange(`F6:F${lastRow}`).getValues();
  return commitee;
}

export default populateDivChairs;
