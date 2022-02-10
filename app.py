from flask import Flask, render_template, request


from nlp_analysis.named_entity_recognition import textblob_ner, spacy_ner
from nlp_analysis.sentiment_analysis import textblob_sentiment_analysis, vader_sentiment_analysis
from nlp_analysis.summarization import spacy_summarization, sumy_summarization


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/named-entity-recognition', methods=['GET', 'POST'])
def named_entiry_recognition():
    if request.method == 'POST':
       input_text = request.form['input_text']
        
       textblob_output = textblob_ner(input_text)
       spacy_output = spacy_ner(input_text)
       
       return render_template('named_entity.html', textblob_output=textblob_output, spacy_output=spacy_output)
    else:
       return render_template('named_entity.html')


@app.route('/sentiment-analysis', methods=['GET', 'POST'])
def sentiment_analysis():
    if request.method == 'POST':
       input_text = request.form['input_text']
        
       textblob_output = textblob_sentiment_analysis(input_text)
       vader_output = vader_sentiment_analysis(input_text)

       return render_template('sentiment_analysis.html', textblob_output=textblob_output, vader_output=vader_output)
    else:
       return render_template('sentiment_analysis.html')


@app.route('/summarization', methods=['GET', 'POST'])
def summarization():
    if request.method == 'POST':
       input_text = request.form['input_text']
        
       spacy_output = spacy_summarization(input_text)
       sumy_output = sumy_summarization(input_text)

       return render_template('summarization.html', spacy_output=spacy_output, sumy_output=sumy_output)
    else:
       return render_template('summarization.html')


if __name__ == '__main__':
   app.run(debug=True)