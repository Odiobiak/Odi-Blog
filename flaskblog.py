
from flask import Flask, render_template
app = Flask(__name__)

#creating a post!
posts = [
    {
        'author' : 'Odiche Obiakarije',
        'title': 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'April 20, 2019'
    },
    {
        'author' : 'Grace Daniels',
        'title': 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'April 21, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


#for continuous runing stuff. help so you dont have to quit and reconnect over nd over again!
if __name__ == '__main__':
    app.run(debug=True)