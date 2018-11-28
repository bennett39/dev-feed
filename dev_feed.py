import requests

from datetime import datetime, date
from secrets import api_key

url = "https://cloud.feedly.com/v3/categories"

r = requests.get(url, headers=api_key)

print(r.status_code)
        
file_name = datetime.now().strftime('%M%S') + ".txt"
f = open(file_name, "w")

lines = [
    str(r.content),
]

f.writelines(lines)
f.close()
