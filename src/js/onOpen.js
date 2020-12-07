import showSidebar from './showSidebar';

const onOpen = () => {
  SpreadsheetApp.getUi()
    .createMenu('📥 Thesis Embargo')
    .addItem('Show Sidebar', 'showSidebar')
    // .addSeparator()
    .addToUi();
  showSidebar();
};

export default onOpen;
