import time

from textblob import TextBlob
import spacy 
try:
    nlp = spacy.load("en_core_web_sm")
except: # If not present, download
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def textblob_ner(input_text):
    textblob_output = {}
    start_time = time.time()
    
    text = TextBlob(input_text)
    textblob_output['ner'] = text.noun_phrases
    
    textblob_output['total_time'] = time.time() - start_time
    
    return textblob_output

def spacy_ner(input_text):
    spacy_output = {}
    start_time = time.time()
    
    doc = nlp(input_text)
    spacy_output['ner'] = doc.ents
    
    spacy_output['total_time'] = time.time() - start_time
    
    return spacy_output