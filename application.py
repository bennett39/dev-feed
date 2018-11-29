import json

with open("sample.json", mode="r", encoding="utf-8") as f:
    data = json.load(f)
f.close()

for i in data['items']:
    print(f"{i['title']} - {i['origin']['title']}")
