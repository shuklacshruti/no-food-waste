import food from './unsplash_FguE8P699zw.png';
import background from "./unsplash_FguE8P699zw.jpg";
import React from 'react';
import './App.css'; // Assuming you have a CSS file for styling

const App = () => {
  const styles = {


  }
  return (
    <div className="container">
      <div className="left-side">
        {/* Content for the left side */}
        <div class="bg-img" style={{ backgroundImage: `url(${background})`,
          backgroundSize: "cover",
          objectFit: "fill",
          height: "100%"}}>
        </div>
      </div>

      <div className="right-side">
        {/* Content for the right side */}
        <h1>Let's Get You Connected</h1>
        <p>Lorem ipsum dolor sit amet consectetur. Aliquam pharetra vel tempus a ac in enim.</p>
        <div className="buttons">
          <button>Donor</button>
          <button>Recipient</button>
        </div>
      </div>
    </div>
  );
};

export default App;
