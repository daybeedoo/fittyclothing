from flask import Flask, render_template, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():



    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))

    # form = LoginForm()

    # if form.validate_on_submit():
    #     user = User()
    #     login_user(user, remember = form.remember_me.data)
    #     next_page = request.args.get('next')
    #     if not next_page or url_parse()





    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

if __name__=='__main__':
    app.run(debug=True)