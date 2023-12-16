from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

users = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['pwd']

    for user in users:
        if user['email'] == email and user['password'] == password:
            return redirect(url_for('success'))

    return 'Email ou senha incorretos.', 401

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    password = request.form['pwd']

    for user in users:
        if user['email'] == email:
            return 'Email já cadastrado.', 401

    users.append({'email': email, 'password': password})

    return redirect(url_for('success'))

@app.route('/success')
def success():
    return 'Logado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
