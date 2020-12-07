const createPDF = () => {
  const studentName = 'Cal T. Beaver';
  const thesisTitle = 'Scientific Sciences';
  // const advisor_name = 'Advi Sor';
  // const division = 'STEM';
  // const grad_year = '2020';
  // const go_approval_date = '01/01/2021';
  // const requestor = 'itme';
  // const reason = 'because reasons etc';
  // const abstract_yn = 'no';

  const template = DriveApp.getFileById(
    PropertiesService.getDocumentProperties().getProperty('TEMPLATE_ID')
  );
  const tempFolder = DriveApp.getFolderById(
    PropertiesService.getDocumentProperties().getProperty('TEMP_FOLDER_ID')
  );

  const pdfFolder = DriveApp.getFolderById(
    PropertiesService.getDocumentProperties().getProperty('PDF_FOLDER_ID')
  );

  const placeholder = template.makeCopy(tempFolder);
  const tempFile = DocumentApp.openById(placeholder.getId());
  const body = tempFile.getBody();
  body.replaceText('{student_name}', studentName);
  body.replaceText('{thesis_title}', thesisTitle);
  tempFile.saveAndClose();

  // Convert tempFile to PDF
  const pdfBlob = tempFile.getAs(MimeType.PDF);
  // eslint-disable-next-line no-unused-vars
  const [WEEK, MM, DD, YYYY] = new Date().toDateString('en-US').split(' ');
  pdfFolder
    .createFile(pdfBlob)
    .setName(`Embargo Exception Request - ${studentName}-${YYYY}-${MM}-${DD}`);

  // Move temp file to Trash
  Drive.Files.remove(placeholder.getId());
};

export default createPDF;
