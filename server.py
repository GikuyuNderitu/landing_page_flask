from flask import Flask, render_template, redirect

app = Flask(__name__)

debug = True

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=debug)
