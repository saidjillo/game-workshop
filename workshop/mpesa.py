# mpesa making requests to get access token
import requests
from requests.auth import HTTPBasicAuth
import json


consumer_key = 'ojDr5pKayBHvpGh3aQt27GMr5ZialWYq'
consumer_secret_key = 'QqFQJAyJZLpod5QK'

# url
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret_key))


json_data = json.loads(r.text)
access_token = json_data.get('access_token', None)

api_url = "http://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
headers = {"Authorization": "Bearer %s" % access_token}
request = { "ShortCode": "600221",
    "ResponseType": " ",
    "ConfirmationURL": "http://127.0.0.1:8000/confirmation",
    "ValidationURL": ""}

response = requests.post(api_url, json = request, headers=headers)

print (response.text)
