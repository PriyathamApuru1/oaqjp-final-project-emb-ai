import requests 
import json

def emotion_detector(text_to_analyze): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    emotionsDict = {}

    if response.status_code == 400:
        emotionsDict = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return emotionsDict   

    formatted_response = json.loads(response.text)

    emotionsDict = formatted_response['emotionPredictions'][0]['emotion']
    
    dominantEmotion = max(emotionsDict, key = emotionsDict.get)
    emotionsDict['dominant_emotion'] = dominantEmotion
    return emotionsDict
    