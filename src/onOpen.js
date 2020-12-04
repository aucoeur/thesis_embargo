const onOpen = () => {
  SpreadsheetApp.getUi()
    .createMenu('📥 AutoMagical')
    .addItem('Show Sidebar', 'showSidebar')
    .addSeparator()
    .addItem('Credits', 'showCredits')
    .addToUi();
};

export default onOpen;
