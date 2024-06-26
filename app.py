from flask import Flask, request, render_template
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import nltk

# Download necessary NLTK data
nltk.download('vader_lexicon')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    input_text = request.form['inputText']
    
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(input_text)
    textblob_analysis = TextBlob(input_text)
    textblob_polarity = textblob_analysis.sentiment.polarity
    textblob_subjectivity = textblob_analysis.sentiment.subjectivity
    
    return render_template('index.html', sentiment_scores=sentiment_scores, 
                           textblob_polarity=textblob_polarity, textblob_subjectivity=textblob_subjectivity,
                           input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)