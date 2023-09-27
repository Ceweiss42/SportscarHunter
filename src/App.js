import React from 'react';
import { useState, useCallback} from 'react';
import logo from './logo.svg';
import './App.css';
import Card from './components/Card';
import Webcam from 'react-webcam';

function App() {

  const vc = {
    facingMode: { exact: "environment" }
  }

  const webcamRef = React.useRef(null);
  const [imageSrc, setImageSource] = useState("NoSource");
  const capture = useCallback(
    () => {
      setImageSource(webcamRef.current.getScreenshot());
      console.log(imageSrc);
      fetch("https://c927-107-185-101-105.ngrok-free.app/testing")
  .then(response => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then(data => {
    // Log the entire data object to the console for debugging
    console.log(data);
    
    // Check if the "message" field exists in the data
    if (data.hasOwnProperty("message")) {
      setImageSource(data.message);
    } else {
      console.error("The 'message' field is missing in the JSON response.");
    }
  })
  .catch(error => {
    console.error("There was a problem with the fetch operation:", error);
  });
    },
    [webcamRef]
  );



  return (
    <div className="App">
      <Webcam ref={webcamRef} screenshotFormat="image/jpeg" videoConstraints={vc}/>
      <button onClick={capture}>click me </button> 
      <p>{imageSrc}</p>
      <Card make="Ferrari" rarity={100} model="250 Testa Rossa" generation="1957-1961"/>
    </div>
  );
}

export default App;
