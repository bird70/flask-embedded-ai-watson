# Flask app: receives user input text, and analyzes text 
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
# Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
# Input json: { "raw_document": { "text": text_to_analyse } }


app = Flask("Emotion Detector")
@app.route('/emotionDetector')
def search_response():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    # Error handling when emotion is None
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    else:
        anger = response["anger"]
        disgust = response["disgust"]
        fear = response["fear"]
        joy = response["joy"]
        sadness = response["sadness"]
        dominant_emotion = response["dominant_emotion"]

    return (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    return render_template("index.html")