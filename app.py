import time
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/named-entity-recognition', methods=['GET', 'POST'])
def named_entiry_recognition():
    if request.method == 'POST':
       input_text = request.form['input-text']
        
       # Library 1 analysis
       start_time = time.time()
       total_time = time.time() - start_time
        
       library_1_output = {total_time}
        
       # Library 2 analysis
       start_time = time.time()
       total_time = time.time() - start_time
        
       library_2_output = {total_time}
       
       return render_template('named_entity.html', library_1_output, library_2_output)
    else:
       return render_template('named_entity.html')


@app.route('/sentiment-analysis', methods=['GET', 'POST'])
def sentiment_analysis():
    if request.method == 'POST':
       input_text = request.form['input-text']
        
       # Library 1 analysis
       start_time = time.time()
       total_time = time.time() - start_time

       library_1_output = {total_time}

       # Library 2 analysis
       start_time = time.time()
       total_time = time.time() - start_time

       library_2_output = {total_time}

       return render_template('sentiment_analysis.html', library_1_output, library_2_output)
    else:
       return render_template('sentiment_analysis.html')


@app.route('/summarization', methods=['GET', 'POST'])
def summarization():
    if request.method == 'POST':
       input_text = request.form['input-text']
        
       # Library 1 analysis
       start_time = time.time()
       total_time = time.time() - start_time

       library_1_output = {total_time}

       # Library 2 analysis
       start_time = time.time()
       total_time = time.time() - start_time

       library_2_output = {total_time}

       return render_template('summarization.html', library_1_output, library_2_output)
    else:
       return render_template('summarization.html')


if __name__ == '__main__':
   app.run(debug=True)