import React from 'react';
import { HashRouter as Router, Route } from 'react-router-dom';

import Header from './components/Header/Header';
import GenerateForm from './components/GenerateForm/GenerateForm';
import ReviewForm from './components/ReviewForm/ReviewForm';


import './App.scss';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Route exact path="/" component={GenerateForm} />
        <Route path="/review" component={ReviewForm} />
      </div>
    </Router>
  )
}

export default App;
