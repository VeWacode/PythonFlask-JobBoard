from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def TopAuthors():
    return render_template('index.hmtl')