import numpy as np
import pandas as pd

import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text
import re

# Preprocessing user inputs with keywords for efficient response mapping
def preprocess_sentences(input_sentences):
    return [re.sub(r'(covid-19|covid)', 'coronavirus', input_sentence, flags=re.I) 
            for input_sentence in input_sentences]

def response(input_sentence):
    # Load module containing USE
    module = hub.load('https://tfhub.dev/google/universal-sentence-encoder-multilingual-qa/3')

    pd.set_option('max_colwidth', 200)  # Increase column width
    data = pd.read_excel("/content/dataset.xlsx")

    # Create response embeddings
    response_encodings = module.signatures['response_encoder'](
            input=tf.constant(preprocess_sentences(data.Answer)),
            context=tf.constant(preprocess_sentences(data.Context)))['outputs']

    test_question = [input_sentence]
    question_encodings = module.signatures['question_encoder'](tf.constant(preprocess_sentences(test_question)))['outputs']
    # Get the response
    test_responses = data.Answer[np.argmax(np.inner(question_encodings, response_encodings), axis=1)]
    return test_responses