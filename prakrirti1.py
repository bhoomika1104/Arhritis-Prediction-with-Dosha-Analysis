from flask import Flask, request, jsonify
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Define Prakriti types and their descriptions
prakriti_types = {
    "Vata": "Vata types are typically energetic, creative, and enthusiastic.",
    "Pitta": "Pitta types are usually intelligent, ambitious, and determined.",
    "Kapha": "Kapha types tend to be calm, steady, and compassionate."
}

# Define features and labels for Prakriti classification
features = [
    [0, 1, 0],  # Vata features: Low Vata, Medium Pitta, Low Kapha
    [1, 0, 0],  # Pitta features: Medium Vata, Low Pitta, Low Kapha
    [0, 0, 1],  # Kapha features: Low Vata, Low Pitta, High Kapha
    # Add more feature vectors for each Prakriti type as needed
]
labels = ['Vata', 'Pitta', 'Kapha']

# Train a decision tree classifier
classifier = DecisionTreeClassifier()
classifier.fit(features, labels)

# Function to process user query and classify Prakriti type
def process_query(query):
    # Dummy feature extraction (replace with actual feature extraction logic)
    # For simplicity, we assume the query contains information about Vata, Pitta, and Kapha
    features = [0, 0, 0]
    if "vata" in query.lower():
        features[0] = 1
    if "pitta" in query.lower():
        features[1] = 1
    if "kapha" in query.lower():
        features[2] = 1
    
    # Classify Prakriti type
    prakriti_type = classifier.predict([features])[0]
    
    # Generate response
    response = {
        'message': prakriti_types[prakriti_type]
    }
    
    return response

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    query = data['query']
    
    response = process_query(query)
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
