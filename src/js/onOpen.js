const onOpen = () => {
  SpreadsheetApp.getUi()
    .createMenu('📥 Thesis Embargo')
    .addItem('Show Sidebar', 'showSidebar')
    .addSeparator()
    .addItem('Credits', 'showCredits')
    .addToUi();
};

export default onOpen;
