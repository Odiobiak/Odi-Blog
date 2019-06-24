from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy 
from forms import LoginForm, RegistrationForm

app = Flask(__name__)

#To set a secret key to avoid invalid access
app.config['SECRET_KEY'] = 'fc5737e4e9c32412f223f91277f72b62'

#creating a post!
posts = [{
    'author': 'Odiche Obiakarije',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'April 20, 2019'
}, {
    'author': 'Grace Daniels',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'April 21, 2019'
}]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


#creating a route for register and login feature
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()  #creating an instance of the form
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login",  methods=['GET', 'POST'])
def login():
    form = LoginForm()  #creating an instance of the form.py
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data =='password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/Author-Note")
def author_note():
    return render_template('author_note.html')


#for continuous run. help so you dont have to quit and reconnect over nd over again!
if __name__ == '__main__':
    app.run(debug=True)
