from flask import Flask, render_template, redirect, url_for, request, session, flash
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template('home.html')

@app.route('/about')
def about():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template('about.html')

@app.route('/shop')
def shop():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template('shop.html')

@app.route('/contact')
def contact():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template('contact.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] != 'admin':
            flash('Invalid Credentials. Please try again.')
            return redirect(url_for('login'))
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html')

if __name__=='__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)