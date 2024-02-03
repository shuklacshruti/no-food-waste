import React, { useState, useEffect } from 'react';

function Matches() {
    const [matches, setMatches] = useState([]);
    const [itemType, setItemType] = useState(""); // State for item type input
    const [itemLocation, setItemLocation] = useState(""); // State for item location input

    // Function to handle fetching matches based on itemType and itemLocation
    const fetchMatches = () => {
        if (itemType && itemLocation) {
            const queryParams = `type=${encodeURIComponent(itemType)}&location=${encodeURIComponent(itemLocation)}`;
            fetch(`http://localhost:5000/api/find_matches?${queryParams}`)
                .then(response => response.json())
                .then(data => {
                    setMatches(data);
                })
                .catch(error => console.error('Error fetching matches:', error));
        }
    };

    // useEffect hook to fetch matches when itemType or itemLocation changes
    useEffect(() => {
        fetchMatches();
    }, [itemType, itemLocation]); // Dependency array includes itemType and itemLocation

    return (
        <div>
            <h2>Find Matches</h2>
            <input
                type="text"
                value={itemType}
                onChange={(e) => setItemType(e.target.value)}
                placeholder="Enter item type"
            />
            <input
                type="text"
                value={itemLocation}
                onChange={(e) => setItemLocation(e.target.value)}
                placeholder="Enter item location"
            />
            <button onClick={fetchMatches}>Fetch Matches</button>

            <h2>Matches</h2>
            {matches.length === 0 ? (
                <p>No matches found.</p>
            ) : (
                <ul>
                    {
                    matches.map(match => (
                        <li key={match.id}>
                            {match.type} - {match.location} - Restaurant: {match.restaurantName}
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
}

export default Matches;
