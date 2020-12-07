const properties = PropertiesService.getDocumentProperties();

// Replace with actual IDs found in URLs- ex. https://docs.google.com/document/d/GDOC_TEMPLATE_ID_HERE/edit
// IDs for Docs template file and temp folder (taken from url)
const templateId = '1gNO6vwaMJXnqlo2ZSbBAJQQyspRn34tFTz75Q9G3MGY';
const tempFolderId = '10KhFWWlsTdabBziMA3QnNxlZBOVWXijM';
const pdfFolderId = '1ZwA_68Thu7W0f32WQ1CgvJ_SbL9vJqhM';

properties.setProperties({
  TEMPLATE_ID: templateId,
  TEMP_FOLDER_ID: tempFolderId,
  PDF_FOLDER_ID: pdfFolderId,
});
