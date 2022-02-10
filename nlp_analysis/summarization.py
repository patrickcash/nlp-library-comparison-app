import time
from heapq import nlargest

import spacy 
nlp = spacy.load('en_core_web_sm')
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def spacy_summarization(input_text):
    spacy_output = {}
    start_time = time.time()
    
    doc = nlp(input_text)
    stopwords = list(STOP_WORDS)
    
    # Find significant wordsbased on frequency
    word_frequencies = {}  
    for word in doc:  
        if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1


    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    
    # score sentences based on significant words
    sentence_list = [ sentence for sentence in doc.sents ]    
    sentence_scores = {}  
    for sent in sentence_list:  
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]


    # use the top 5 sentences as a summary
    summarized_sentences = nlargest(5, sentence_scores, key=sentence_scores.get)
    summary_sentences = [ w.text for w in summarized_sentences ]
    spacy_output['summary'] = ' '.join(summary_sentences)
    
    spacy_output['total_time'] = time.time() - start_time
    
    return spacy_output

def sumy_summarization(input_text):
    sumy_output = {}
    start_time = time.time()
    
    parser = PlaintextParser.from_string(input_text, Tokenizer("english"))
    
    # using Lexrank summarizer that is similair to the spacy approach used above
    lex_summarizer = LexRankSummarizer()
    
    # Use the top 5 senteences as a sumart
    summarized_sentences = lex_summarizer(parser.document, 5)
    summary_sentences = [str(sentence) for sentence in summarized_sentences]
    sumy_output['summary'] = ' '.join(summary_sentences)
    
    sumy_output['total_time'] = time.time() - start_time
    
    return sumy_output