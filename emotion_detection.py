'''
Emotion detection using Watson AI
'''
import requests
import json

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    inp_doc = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    response = requests.post(url, json=inp_doc, headers=header)
    print("detection run")

    return response.text


    # response_dict = json.loads(response.text)
    # emotions = response_dict["emotionPredictions"][0]["emotion"]

    # anger = emotions["anger"]
    # disgust = emotions["disgust"]
    # fear = emotions["fear"]
    # joy = emotions["joy"]
    # sadness = emotions["sadness"]
    # emotion_scores = {
    #     "anger": anger,
    #     "disgust": disgust,
    #     "fear": fear,
    #     "joy": joy,
    #     "sadness": sadness
    # }

    # dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # return {
    #     "anger": anger,
    #     "disgust": disgust,
    #     "fear": fear,
    #     "joy": joy,
    #     "sadness": sadness,
    #     "dominant_emotion": dominant_emotion
    # }