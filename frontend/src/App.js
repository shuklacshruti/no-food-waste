// frontend/src/App.js
import React from 'react';
import Matches from './components/Matches';  // Import the Matches component
import FindShelters from './components/FindShelters';
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Welcome to the React-Flask Integration Example.
        </p>
      </header>
      <Matches />  
      <FindShelters /> 
    </div>
  );
}

export default App;
