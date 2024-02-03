// frontend/src/components/FindShelters.js
import React, { useState } from 'react';

function FindShelters() {
    const [city, setCity] = useState('');
    const [foodType, setFoodType] = useState('');
    const [matches, setMatches] = useState([]);

    const findMatches = () => {
        fetch(`http://localhost:5000/api/find_matches?type=${foodType}&location=${city}`)
            .then(response => response.json())
            .then(data => setMatches(data))
            .catch(error => console.error('Error finding matches:', error));
    };

    return (
        <div>
            <ul>
            {matches.map(match => (
                <li key={match.id}>{match.type} - {match.location} - Restaurant: {match.restaurantName}</li>
            ))}
            </ul>
        </div>
    );
}

export default FindShelters;
