from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import LoginForm, RegistrationForm
from flaskblog.models import User, Post


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
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password= hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your Account has been created! you are now able to log in!', 'success')
        return redirect(url_for('login'))
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
