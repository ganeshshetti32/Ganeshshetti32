from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory store for mood entries (replace with database in production)
mood_entries = []

@app.route('/submit_mood', methods=['POST'])
def submit_mood():
    data = request.get_json()
    mood = data.get('mood')
    journal = data.get('journal', '')
    
    if not mood:
        return jsonify({'error': 'Mood is required'}), 400

    entry = {
        'mood': mood,
        'journal': journal,
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    }
    mood_entries.append(entry)

    return jsonify({'message': 'Mood recorded successfully', 'entry': entry}), 201

@app.route('/get_moods', methods=['GET'])
def get_moods():
    return jsonify(mood_entries), 200

if __name__ == '__main__':
    app.run(debug=True)
