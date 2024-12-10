import React, { useState, useEffect } from 'react';
import './App.css';

const API_URL = 'http://127.0.0.1:5000/api';

function App() {
  const [locations, setLocations] = useState([]);
  const [newLocation, setNewLocation] = useState({
    latitude: '',
    longitude: '',
    description: ''
  });

  useEffect(() => {
    fetchLocations();
  }, []);

  const fetchLocations = async () => {
    try {
      const response = await fetch(`${API_URL}/locations`);
      const data = await response.json();
      setLocations(data);
    } catch (error) {
      console.error('Error fetching locations:', error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(`${API_URL}/locations`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newLocation),
      });
      if (response.ok) {
        setNewLocation({ latitude: '', longitude: '', description: '' });
        fetchLocations();
      }
    } catch (error) {
      console.error('Error adding location:', error);
    }
  };

  const handleDelete = async (id) => {
    try {
      const response = await fetch(`${API_URL}/locations/${id}`, {
        method: 'DELETE',
      });
      if (response.ok) {
        fetchLocations();
      }
    } catch (error) {
      console.error('Error deleting location:', error);
    }
  };

  return (
    <div className="App">
      <h1>GPS Location Tracker</h1>
      
      <div className="form-container">
        <h2>Add New Location</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="number"
            step="any"
            placeholder="Latitude"
            value={newLocation.latitude}
            onChange={(e) => setNewLocation({...newLocation, latitude: e.target.value})}
            required
          />
          <input
            type="number"
            step="any"
            placeholder="Longitude"
            value={newLocation.longitude}
            onChange={(e) => setNewLocation({...newLocation, longitude: e.target.value})}
            required
          />
          <input
            type="text"
            placeholder="Description"
            value={newLocation.description}
            onChange={(e) => setNewLocation({...newLocation, description: e.target.value})}
          />
          <button type="submit">Add Location</button>
        </form>
      </div>

      <div className="locations-list">
        <h2>Locations</h2>
        <div className="locations-grid">
          {locations.map((location) => (
            <div key={location.id} className="location-card">
              <h3>{location.description || 'No description'}</h3>
              <p>Latitude: {location.latitude}</p>
              <p>Longitude: {location.longitude}</p>
              <p>Added: {new Date(location.timestamp).toLocaleString()}</p>
              <button onClick={() => handleDelete(location.id)} className="delete-btn">
                Delete
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
