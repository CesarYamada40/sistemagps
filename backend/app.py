from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import sqlite3
import datetime
import os

app = Flask(__name__)
CORS(app)

# Configuração do banco de dados SQLite
DATABASE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'locations.db')

def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS locations
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         latitude REAL NOT NULL,
         longitude REAL NOT NULL,
         description TEXT,
         timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)
    ''')
    conn.commit()
    conn.close()

# Inicializa o banco de dados
init_db()

@app.route('/')
def home():
    return jsonify({"message": "GPS Location Tracker API", "status": "running"})

@app.route('/api/locations', methods=['GET'])
def get_locations():
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM locations ORDER BY timestamp DESC')
    locations = [{'id': row[0], 'latitude': row[1], 'longitude': row[2], 
                 'description': row[3], 'timestamp': row[4]} 
                for row in c.fetchall()]
    conn.close()
    return jsonify(locations)

@app.route('/api/locations', methods=['POST'])
def add_location():
    data = request.json
    if not data or 'latitude' not in data or 'longitude' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute('INSERT INTO locations (latitude, longitude, description) VALUES (?, ?, ?)',
             (data['latitude'], data['longitude'], data.get('description', '')))
    conn.commit()
    location_id = c.lastrowid
    conn.close()
    return jsonify({'id': location_id, 'message': 'Location added successfully'}), 201

@app.route('/api/locations/<int:id>', methods=['DELETE'])
def delete_location(id):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM locations WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Location deleted successfully'})

@app.route('/api/locations/<int:id>', methods=['PUT'])
def update_location(id):
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute('UPDATE locations SET latitude = ?, longitude = ?, description = ? WHERE id = ?',
             (data['latitude'], data['longitude'], data.get('description', ''), id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Location updated successfully'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
