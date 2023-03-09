import flask
import io
import string
import time
import os
import numpy as np
import torch
from flask import Flask, jsonify, request
from DeepLearningExamples.PyTorch.SpeechSynthesis.Tacotron2 import inference
from config import args, parser

app = Flask(__name__)

# Build Routes

@app.route('/predict', methods=['POST'])
def tts():    
    text = request.form['text']

    if not text:
        return

    args.input_text=text

    audio=inference.main(args, parser)

    return audio    

@app.route('/', methods=['GET'])
def index():
    return 'Machine Learning Inference'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
