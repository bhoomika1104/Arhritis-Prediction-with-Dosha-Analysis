from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    user_query = data['query']

    # Process user query (add your chatbot logic here)
    # ...

    # Return a response to the web interface
    bot_response = f"Received: {user_query}"
    return jsonify({'message': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
