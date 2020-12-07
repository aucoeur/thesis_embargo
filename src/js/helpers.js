const getLastRowInCol = (col) => {
  let rowNum = 0;
  let blank = false;
  for (let row = 0; row < col.length; row += 1) {
    if (col[row][0] === '' && !blank) {
      rowNum = row;
      blank = true;
    } else if (col[row][0] !== '') {
      blank = false;
    }
  }
  return rowNum;
};

export default getLastRowInCol;
