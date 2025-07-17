#https://learn.microsoft.com/en-us/azure/ai-services/translator/text-translation/quickstart/rest-api?tabs=python
import requests, uuid, json
import os
import dotenv

# Load environment variables
dotenv.load_dotenv()
TRANSLATION_API_KEY = os.getenv("TRANSLATION_API_KEY")

# Add your key and endpoint
key = TRANSLATION_API_KEY
endpoint ="https://api.cognitive.microsofttranslator.com"
# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = "eastus2" #"<YOUR-RESOURCE-LOCATION>"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['fr', 'zu']
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    #'text': 'I would really like to drive your car around the block a few times!'
    'text': "hi my name is phillip and im from texas! where are you from"
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

# Save the response to a file text file
with open('translation_response.txt', 'w', encoding='utf-8') as f:
    for item in response:
        for translation in item.get('translations', []):
            f.write(f"Translated to {translation['to']}: {translation['text']}\n")

# 👉 work with copilot to generate and save to text to speech