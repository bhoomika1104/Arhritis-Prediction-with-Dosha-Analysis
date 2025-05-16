from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Process user input and generate chatbot response
    user_input = request.form['user_input']
    # Implement chatbot logic here
    chatbot_response = f'You said: {user_input}'  # Example response
    return chatbot_response

if __name__ == '__main__':
    app.run(debug=True)
