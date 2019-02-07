from apscheduler.schedulers.background import BackgroundScheduler
import markovify
import time
from flask import Flask, render_template, jsonify
import random
app = Flask(__name__, static_url_path='/static')

nyc = open("nyc_connections.txt").read()
longings = open("longings.txt").read()

@app.route('/')
def home():
    poem = generate_poem()
    return render_template('index.html', poem=poem)

@app.route('/more_connections/')
def more_connectionse():
    poem = generate_poem()
    return jsonify({'poem': poem})

def generate_poem():
    ny = markovify.Text(nyc)
    longing = markovify.Text(longings)
    combo = markovify.combine([ny, longing], [.7, .3])
    poem = []

    for i in range(random.randint(2, 6)):
        poem.append(combo.make_short_sentence(100, state_size=12, tries=100))

    return poem

class SentencesByChar(markovify.Text):
    def word_split(self, sentence):
        return list(sentence)
    def word_join(self, words):
        return "".join(words)

def by_char():
    longing_model = SentencesByChar(longings, state_size=7)
    ny_model = SentencesByChar(nyc, state_size=7)
    poem = []
    
    combo = markovify.combine([ny_model, longing_model], [.8, .2])
    # print(combo.make_sentence(state_size=7, tries=100))

    for i in range(random.randint(2, 6)):
        poem.append(combo.make_sentence(state_size=10, tries=100))
    return poem
    
