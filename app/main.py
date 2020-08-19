from flask import Flask, render_template, redirect, url_for, request, session, flash
import os

app = Flask(__name__)

@app.route('/')
def home():
    return loggedcheck('home')

@app.route('/about')
def about():
    return loggedcheck('about')

@app.route('/shop')
def shop():
    return loggedcheck('shop')

@app.route('/contact')
def contact():
    return loggedcheck('contact')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] != 'admin':
            flash('Invalid Credentials. Please try again.')
            return redirect(url_for('login'))
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))
    try:
        if session['logged_in'] == True:
            return redirect(url_for('home'))
    except KeyError:
        return render_template('login.html')

def loggedcheck(name):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template(name + '.html')

if __name__=='__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)