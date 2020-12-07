// Rename this file to config.js

const properties = PropertiesService.getDocumentProperties();

// Replace with actual IDs found in URLs- ex. https://docs.google.com/document/d/GDOC_TEMPLATE_ID_HERE/edit

const templateId = '1L5tdBb7pHV1drylOJLU153SPvAP4xV8H';
const tempFolderId = '1L5tdBb7pHV1drylOJLU153SPvAP4xV8H';
const pdfFolderId = '1L5tdBb7pHV1drylOJLU153SPvAP4xV8H';

properties.setProperties({
  TEMPLATE_ID: templateId,
  TEMP_FOLDER_ID: tempFolderId,
  PDF_FOLDER_ID: pdfFolderId,
});
