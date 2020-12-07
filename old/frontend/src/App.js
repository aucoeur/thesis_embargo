import React from 'react';

import Header from './components/Header/Header';
import GenerateForm from './components/GenerateForm/GenerateForm';
import ReviewForm from './components/ReviewForm/ReviewForm';


import './App.scss';

function App() {
  return (
      <div className="App">
        <Header />
        <GenerateForm />
      </div>
  )
}

export default App;
