const showSidebar = () => {
  const template = HtmlService.createTemplateFromFile('index');
  const html = template.evaluate().setTitle('Thesis Embargo');
  SpreadsheetApp.getUi().showSidebar(html);
};

export default showSidebar;
