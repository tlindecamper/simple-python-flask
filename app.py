from flask import Flask, render_template
from flask_heroku import Heroku

app = Flask (__name__)

@app.route('/')
def home():
    return render_template("home.html")
    app.route('/second_page')
def second_page():
    return render_template('second_page.html')

if __name__ == "__name__":
    app.run(debug=True)
