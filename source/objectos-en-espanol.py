#!/usr/bin/env python

# importing the requests library
import requests

# defining the api-endpoint
API_ENDPOINT = "https://www.googleapis.com/language/translate/v2"

# your API key here
API_KEY = "AIzaSyDzvkjS7zn7WqucXeJ5_yoARbZj4afSXVo"

# sending post request and saving response as response object
r = requests.post(url=API_ENDPOINT, data={'key': API_KEY, 'source': 'en', 'target': 'es', 'q': 'Hello World'})

# extracting response text
pastebin_url = r.text
print("The pastebin URL is:%s" % pastebin_url)

print('hello bitches')

#curl "https://www.googleapis.com/language/translate/v2?key=AIzaSyDzvkjS7zn7WqucXeJ5_yoARbZj4afSXVo&source=en&target=es&q=Hello%20World"
