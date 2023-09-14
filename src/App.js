import React from 'react';
import logo from './logo.svg';
import './App.css';
import Card from './components/Card';
import Webcam from 'react-webcam';

function App() {

  const vc = {
    facingMode: { exact: "environment" }
  }
  return (
    <div className="App">
      <Webcam videoConstraints={vc}/>
      <Card make="Ferrari" rarity={100} model="250 Testa Rossa" generation="1957-1961"/>
    </div>
  );
}

export default App;
