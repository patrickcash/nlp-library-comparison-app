import time

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def textblob_sentiment_analysis(input_text):
    textblob_output = {}
    start_time = time.time()
    
    text = TextBlob(input_text)
    textblob_output['sentiment'] = text.sentiment
    
    textblob_output['total_time'] = time.time() - start_time
    
    return textblob_output

def vader_sentiment_analysis(input_text):
    vader_output = {}
    start_time = time.time()
    
    analyzer = SentimentIntensityAnalyzer()
    vader_output['sentiment'] = analyzer.polarity_scores(input_text)
    
    vader_output['total_time'] = time.time() - start_time
    
    return vader_output