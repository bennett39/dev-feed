import requests

from datetime import datetime, date
from secrets import api_key

# Main Feedly API. Use sandbox.feedly.com for testing.
# https://developer.feedly.com/
url_base = "https://cloud.feedly.com/v3/streams/contents"

# Dictionary to feed into requests module to create URL
# e.g. - "/v3/streams/contents?streamId=feed%2Fhttp..."
payload = {
    "streamId": "feed/http://feeds.engadget.com/weblogsinc/engadget/"
}

# Get API response using requests module - requests must be installed
r = requests.get(url_base, headers=api_key, params=payload)

# Status message for user on command line
message = f"URL: {r.url} \nStatus: {r.status_code}"
print(message)

# Store the results of the API call in a text file
file_name = datetime.now().strftime('%M%S') + ".txt"
f = open(file_name, "w")

# If you need access to more information (e.g. r.text, r.encoding, etc),
# then add those here as lines in the output text file.
lines = [
    str(r.content),
]
f.writelines(lines)
f.close()