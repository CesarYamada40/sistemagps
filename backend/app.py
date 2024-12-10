Defaulting to user installation because normal site-packages is not writeable
Collecting Flask==2.0.1 (from -r requirements.txt (line 1))
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
locations = [
    {'id': 1, 'name': 'Location 1', 'latitude': 40.7128, 'longitude': -74.0060},
    {'id': 2, 'name': 'Location 2', 'latitude': 34.0522, 'longitude': -118.2437}
]

@app.route('/locations', methods=['GET'])
def get_locations():
    return jsonify({'locations': locations})

@app.route('/locations', methods=['POST'])
def add_location():
    new_location = request.get_json()
    locations.append(new_location)
    return jsonify(new_location), 201

@app.route('/locations/<int:location_id>', methods=['PUT'])
def update_location(location_id):
    location = next((loc for loc in locations if loc['id'] == location_id), None)
    if location is None:
        return jsonify({'error': 'Location not found'}), 404

    data = request.get_json()
    location.update(data)
    return jsonify(location)

@app.route('/locations/<int:location_id>', methods=['DELETE'])
def delete_location(location_id):
    global locations
    locations = [loc for loc in locations if loc['id'] != location_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
