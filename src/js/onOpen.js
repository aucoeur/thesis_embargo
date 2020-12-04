import showSidebar from './showSidebar';

const onOpen = () => {
  SpreadsheetApp.getUi()
    .createMenu('📥 Thesis Embargo')
    .addItem('Show Sidebar', 'showSidebar')
    .addSeparator()
    .addItem('Credits', 'showCredits')
    .addToUi();
  showSidebar();
};

export default onOpen;
