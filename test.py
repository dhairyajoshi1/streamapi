import json
import httpx

url = 'http://127.0.0.1:8000/'

with httpx.stream('GET', url) as r:
    for chunk in r.iter_raw():
        print(json.loads(chunk))