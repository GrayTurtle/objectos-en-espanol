#!/usr/bin/env python

#curl "https://www.googleapis.com/language/translate/v2?key=AIzaSyDzvkjS7zn7WqucXeJ5_yoARbZj4afSXVo&source=en&target=es&q=Hello%20World"
#curl -v -s -H "Content-Type: application/json" https://vision.googleapis.com/v1/images:annotate?key=AIzaSyDzvkjS7zn7WqucXeJ5_yoARbZj4afSXVo --data-binary @request.json

import requests
import json

API_KEY = "AIzaSyDzvkjS7zn7WqucXeJ5_yoARbZj4afSXVo"
API_VISION = "https://vision.googleapis.com/v1/images:annotate"
API_TRANSLATE = "https://www.googleapis.com/language/translate/v2"

payload = {
  "requests": [
    {
      "image": {
        "source": {
          "imageUri": "https://cloud.google.com/vision/images/rushmore.jpg"
        }
      },
      "features": [
        {
          "type": "LANDMARK_DETECTION",
          "maxResults": 1
        },
        {
          "type": "WEB_DETECTION",
          "maxResults": 2
        }
      ]
    }
  ]
}


vision_request = requests.post(url=API_VISION, params={'key': API_KEY}, headers={'Content-Type': 'application/json'}, data=json.dumps(payload))
translate_request = requests.post(url=API_TRANSLATE, data={'key': API_KEY, 'source': 'en', 'target': 'es', 'q': 'Hello World'})

print(vision_request.text)
print(translate_request.text)
