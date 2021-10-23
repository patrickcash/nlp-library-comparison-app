from logging import debug
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/named-entity-recognition')
def named_entiry_recognition():
    return render_template('named_entity.html')


@app.route('/sentiment-analysis')
def sentiment_analysis():
    return render_template('sentiment_analysis.html')


@app.route('/summarization')
def summarization():
    return render_template('summarization.html')


if __name__ == '__main__':
    app.run(debug=True)