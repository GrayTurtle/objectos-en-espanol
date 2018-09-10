#!/usr/bin/env python

#curl "https://www.googleapis.com/language/translate/v2?key=AIzaSyDzvkjS7zn7WqucXeJ5_yoARbZj4afSXVo&source=en&target=es&q=Hello%20World"
#curl -v -s -H "Content-Type: application/json" https://vision.googleapis.com/v1/images:annotate?key=AIzaSyDzvkjS7zn7WqucXeJ5_yoARbZj4afSXVo --data-binary @request.json

import requests

API_VISION = "https://vision.googleapis.com/v1/images:annotate"
API_TRANSLATE = "https://www.googleapis.com/language/translate/v2"
API_KEY = "AIzaSyDzvkjS7zn7WqucXeJ5_yoARbZj4afSXVo"

vision_request = requests.post(url=API_VISION, data={'key': API_KEY}, headers={'Content-Type': 'application/json'}, files={'file':('request.json', open('request.json', 'rb'))})
translate_request = requests.post(url=API_TRANSLATE, data={'key': API_KEY, 'source': 'en', 'target': 'es', 'q': 'Hello World'})

print(vision_request.text)
print(translate_request.text)
