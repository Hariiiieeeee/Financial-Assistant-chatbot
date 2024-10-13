import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import json
import re
import random

__tokenizer = None
__model = None
__lbl_enc = None
__intents = None


def load_artifacts():
    global __tokenizer
    global __model
    global __lbl_enc
    global __intents

    __model = load_model('chatbot_model.h5')

    with open('tokenizer.pkl', 'rb') as handle:
        __tokenizer = pickle.load(handle)
    
    with open('label_encoder.pkl', 'rb') as handle:
        __lbl_enc = pickle.load(handle)

    with open('intents1.json', 'r') as f:
        __intents = json.load(f)

def preprocess_text(pattern):
    text = []
    txt = re.sub('[^a-zA-Z\']', ' ', pattern)
    txt = txt.lower()
    txt = txt.split()
    txt = " ".join(txt)
    text.append(txt)
    return text


def generate_answer(pattern):
    if pattern.lower() in ['goodbye', 'bye']:
        response = "Goodbye! Have a great day!"
        print(response)
        return response
    
    load_artifacts()

    text = preprocess_text(pattern)

    x_test = __tokenizer.texts_to_sequences(text)
    x_test = pad_sequences([x_test], padding='post', maxlen=__model.input_shape[1])
    y_pred = __model.predict(x_test)
    y_pred = y_pred.argmax()
    tag = __lbl_enc.inverse_transform([y_pred])[0]

    # Get the corresponding responses for the predicted tag
    for intent in __intents['intents']:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            break
    return response
    
