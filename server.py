from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():

    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] == None:
        return "Invalid text! Please try again!"

    emotions = ', '.join(f"'{k}': {v}" for k, v in response.items() if k != 'dominant_emotion')
    responseText = f"For the given statement, the system response is {emotions}. The dominant emotion is {response['dominant_emotion']}."

    return responseText

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)