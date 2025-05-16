from flask import Flask, request, jsonify

app = Flask(__name__)

# Define Prakruti types and their descriptions
prakruti_types = {
    "Vata": "Vata types are typically energetic, creative, and enthusiastic.",
    "Pitta": "Pitta types are usually intelligent, ambitious, and determined.",
    "Kapha": "Kapha types tend to be calm, steady, and compassionate.",
    "Vata-Pitta": "Vata-Pitta types exhibit characteristics of both Vata and Pitta.",
    "Pitta-Kapha": "Pitta-Kapha types exhibit characteristics of both Pitta and Kapha.",
    "Kapha-Vata": "Kapha-Vata types exhibit characteristics of both Kapha and Vata."
}

# Define questions for Prakruti assessment
questions = [
    "Do you tend to have a thin and light build?",
    "Are you prone to dry skin and hair?",
    "Do you have a quick mind but also experience anxiety?",
    "Are you competitive and easily angered?",
    "Do you have a strong appetite and good digestion?",
    "Are you calm, patient, and compassionate?",
    "Do you prefer routine and dislike change?",
    "Are you prone to weight gain and sluggishness?",
]

# Initialize dictionary to store user responses
user_responses = {}

# Function to process user responses and classify Prakruti type
def classify_prakruti(responses):
    vata_count = responses.count("Yes") + responses.count("Sometimes")
    pitta_count = responses.count("Yes") + responses.count("Sometimes")
    kapha_count = responses.count("Yes") + responses.count("Sometimes")
    
    if vata_count > pitta_count and vata_count > kapha_count:
        return "Vata"
    elif pitta_count > vata_count and pitta_count > kapha_count:
        return "Pitta"
    elif kapha_count > vata_count and kapha_count > pitta_count:
        return "Kapha"
    elif vata_count == pitta_count and vata_count > kapha_count:
        return "Vata-Pitta"
    elif pitta_count == kapha_count and pitta_count > vata_count:
        return "Pitta-Kapha"
    elif kapha_count == vata_count and kapha_count > pitta_count:
        return "Kapha-Vata"
    else:
        return "Unknown"

# Route to start Prakruti assessment
@app.route('/start', methods=['POST'])
def start_assessment():
    user_responses.clear()
    response = {"message": questions[0]}
    return jsonify(response)

# Route to handle user responses
@app.route('/respond', methods=['POST'])
def handle_response():
    data = request.json
    question_index = data['question_index']
    response = data['response']
    
    user_responses[question_index] = response
    
    if question_index < len(questions) - 1:
        next_question = questions[question_index + 1]
        response = {"message": next_question}
    else:
        prakruti_type = classify_prakruti(list(user_responses.values()))
        description = prakruti_types[prakruti_type]
        response = {"message": f"Your Prakruti type is {prakruti_type}. {description}"}
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
