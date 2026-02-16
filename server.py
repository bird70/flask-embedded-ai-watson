# Flask app: receives user input text, and analyzes text 
from flask import Flask, request, render_template
from emotion_detection import emotion_detector

# URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
# Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
# Input json: { "raw_document": { "text": text_to_analyse } }

app = Flask("Emotion Detector")
@app.route('/emotionDetector')
def search_response():
        query = request.args.get("text-to-analyze")
        if not query:
            return {"error_message": "Input parameter missing"}, 422    
        # pass the resource to Watson AI    
        resource = emotion_detector(query)
        
        if resource:
            return {"message": resource}
        else:        
            return {"error_message": "Resource not found"},  404
        
@app.route("/")
def render_index_page():
    return render_template("index.html")