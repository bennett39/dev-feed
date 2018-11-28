import requests

from datetime import datetime, date
from secrets import api_key

url_base = "https://cloud.feedly.com/v3/streams/contents"
payload = {
    "streamId": "feed/http://feeds.engadget.com/weblogsinc/engadget/"
}

r = requests.get(url_base, headers=api_key, params=payload)

message = f"URL: {r.url} \nStatus: {r.status_code}"

print(message)
        
file_name = datetime.now().strftime('%M%S') + ".txt"
f = open(file_name, "w")

lines = [
    str(r.content),
]

f.writelines(lines)
f.close()
