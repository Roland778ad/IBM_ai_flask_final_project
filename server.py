"""Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
   localhost:5000."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
from rich import print

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emotion_detection():
    """This code receives the text from the HTML interface,
       processes it through the emotion_detector() function
       and returns a formatted dictionary with the emotions
       and the associated scores.
    """
    # Request input text from front-end html
    text_to_analyze = request.args.get('textToAnalyze')
    # Send the text to emotion_detector function 
    result = emotion_detector(text_to_analyze)
    return f"""For the given statement, the system response is 'anger': {result['anger']}, 
            'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']},
            and 'sadness': {result['sadness']}. The dominant emotion is 
            {result['dominant_emotion']}."""

@app.route('/')
def index_page():
    """This function initiates the main aplication on the page."""
    return render_template('index.html')

if __name__=='__main__':
    # This function executes the flask app and deployes it on localhost:5000
    app.run(host='0.0.0.0', port=5000)