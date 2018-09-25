#!/usr/bin/env python

# This program detects an object using Google Cloud Vision API then translates that object into Spanish using the
# Google Cloud Translate API.
# Author: ['hip', 'hip']!

import requests
import json
import base64
import sys

API_KEY = "API_KEY"
API_VISION = "https://vision.googleapis.com/v1/images:annotate"
API_TRANSLATE = "https://www.googleapis.com/language/translate/v2"

# Convert the image from the argument into a base64 string
with open('images/{}'.format(sys.argv[1]), "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read())

payload = \
    {
        "requests": [
            {
                "image": {
                    "content": encoded_image,
                },
                "features": [
                    {
                        "type": "LABEL_DETECTION",
                        "maxResults": 1
                    }
                ]
            }
        ]
    }

# Post requests to the APIs along with the parsing of the response
vision_request = requests.post(url=API_VISION, params={'key': API_KEY}, headers={'Content-Type': 'application/json'}, data=json.dumps(payload))

if list(vision_request.json()["responses"][0])[0] == "error": 
	print("Error: Bad image")
	sys.exit(0)

english_word = vision_request.json()["responses"][0]["labelAnnotations"][0]["description"].capitalize()

translate_request = requests.post(url=API_TRANSLATE, data={'key': API_KEY, 'source': 'en', 'target': 'es', 'q': english_word})
spanish_word = translate_request.json()["data"]["translations"][0]["translatedText"]

print("English: " + english_word)
print("Spanish: " + spanish_word)
