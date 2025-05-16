from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if password != confirm_password:
        return "Passwords do not match. Please try again."

    # Save user details to CSV file
    with open('users.csv', 'a', newline='') as csvfile:
        fieldnames = ['email', 'password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'email': email, 'password': password})

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
