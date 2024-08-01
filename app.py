from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change this to a random secret key

# Dummy user data
users = {
    'testuser': {
        'username': 'testuser',
        'password': 'password123',
        'name': 'Test User',
        'email': 'testuser@example.com'
    }
}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        
        if user and user['password'] == password:
            session['username'] = user['username']
            return redirect(url_for('profile'))
        else:
            flash('Invalid credentials. Please try again.')
    
    return render_template('login.html')

@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = users[session['username']]
    return render_template('profile.html', user=user)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
