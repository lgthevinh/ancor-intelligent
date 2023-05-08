import requests

def chat_completion(content):
    url = "https://openai80.p.rapidapi.com/chat/completions"
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": str(content)
            }
        ]
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "9b8b9397f1msh626810dee5e8592p17beeajsnce05ecc211c7",
        "X-RapidAPI-Host": "openai80.p.rapidapi.com",
        "Accept-Encoding": "deflate"
    }
    response = requests.post(url, json=payload, headers=headers)
    json_data = response.json()
    return json_data['choices'][0]['message']['content']

def fix_spelling_mistake(content):
    url = "https://openai80.p.rapidapi.com/edits"
    payload = {
        "model": "text-davinci-edit-001",
        "input": str(content),
        "instruction": "Fix the spelling mistakes"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "9b8b9397f1msh626810dee5e8592p17beeajsnce05ecc211c7",
        "X-RapidAPI-Host": "openai80.p.rapidapi.com",
        "Accept-Encoding": "deflate"
    }
    response = requests.post(url, json=payload, headers=headers)
    json_data = response.json()
    return json_data['choices'][0]['text']

def create_image(content):
    url = "https://openai80.p.rapidapi.com/images/generations"
    payload = {
        "prompt": str(content),
        "n": 1,
        "size": "1024x1024"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "9b8b9397f1msh626810dee5e8592p17beeajsnce05ecc211c7",
        "X-RapidAPI-Host": "openai80.p.rapidapi.com",
        "Accept-Encoding": "deflate"
    }
    response = requests.post(url, json=payload, headers=headers)
    json_data = response.json()
    return json_data['data'][0]['url']
