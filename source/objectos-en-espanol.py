#!/usr/bin/env python

#curl "https://www.googleapis.com/language/translate/v2?key=AIzaSyDzvkjS7zn7WqucXeJ5_yoARbZj4afSXVo&source=en&target=es&q=Hello%20World"

import requests

API_VISION = "https://vision.googleapis.com/v1/images:annotate"
API_TRANSLATE = "https://www.googleapis.com/language/translate/v2"
API_KEY = "AIzaSyDzvkjS7zn7WqucXeJ5_yoARbZj4afSXVo"

translate_request = requests.post(url=API_TRANSLATE, data={'key': API_KEY, 'source': 'en', 'target': 'es', 'q': 'Hello World'})

print(translate_request)
