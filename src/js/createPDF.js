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

  const placeholder = template.makeCopy(tempFolder);
  const tempFile = DocumentApp.openById(placeholder.getId());
  const body = tempFile.getBody();
  body.replaceText('{student_name}', studentName);
  body.replaceText('{thesis_title}', thesisTitle);
  tempFile.saveAndClose();
};

export default createPDF;
