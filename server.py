"""Flask server for Emotion Detection."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """Handle emotion detection request."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    emotions = ', '.join(f"'{k}': {v}" for k, v in response.items() if k != 'dominant_emotion')
    response_text = (
        f"For the given statement, the system response is {emotions}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return response_text

@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
