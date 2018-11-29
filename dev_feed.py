import json
import requests

from datetime import datetime, date
from secrets import api_key

# Main Feedly API. Use sandbox.feedly.com for testing.
# Documentation: https://developer.feedly.com/
url_base = "https://cloud.feedly.com/v3/streams/contents"

user_streamId = ("user/c04622d3-e092-4537-b5d5-a326858ffe1d/"
                "category/Tech - Development")

# Dictionary that feeds into requests module to create URL
# e.g. - "/v3/streams/contents?streamId=feed%2Fhttp..."
# Optional: count (default 20), unreadOnly (boolean)
# Documentation:
# https://developer.feedly.com/v3/streams/#get-the-content-of-a-stream
payload = {
    "streamId": user_streamId
}

# Get API response using requests module - requests must be installed
r = requests.get(url_base, headers=api_key, params=payload)

# Prettify JSON
data = json.dumps(r.json(), indent=4)

# Status message for user on command line
message = f"URL: {r.url}\nStatus: {r.status_code}"
print(message)

# Store the results of the API call in a json file
file_name = ("output/" + datetime.now().strftime('%y-%m-%d-%H%M%S') + 
            ".json")

# If you need other data in output file (e.g. r.text, r.encoding), then
# add those as lines here
lines = [
    data,
]

f = open(file_name, mode="w", encoding="utf-8")
f.writelines(lines)
f.close()
