"""This is the main module for the final, emotion detection project 
in IBM Python app development with AI and Flask
"""

import json
import requests

# Create an emotion detector function to send input argument to IBM AI model for analysys
def emotion_detector(text_to_analyse):
    # Define the required elements of the request 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    text_obj = { "raw_document": { "text": text_to_analyse } }
    # Create request to IBM with the defined variables
    response = requests.post(url, json=text_obj, headers=header, timeout=60)
    # Format the response from server to a json dictionary
    formatted_response = json.loads(response.text)
    # Filter the response to only the required information, and preserve it in a dictionary
    filtered_response = formatted_response['emotionPredictions'][0]['emotion']
    # Find and add the dominant emotion to the filtered responses
    filtered_response['dominant_emotion'] = max(filtered_response, key=filtered_response.get)
    # Return formatted json with all required items
    return filtered_response

text_to_analyze = 'I love this new technology.'
print(emotion_detector(text_to_analyze))

