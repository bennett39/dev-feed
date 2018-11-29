import json

# TODO - still having touble with utf-8 encoding errors. Had to clean
# sample.json in order to work with it for now. Long term, need a fix.
with open("sample.json", mode="r", encoding="utf-8") as f:
    data = json.load(f)
f.close()

# Use sample-pretty.json to see the structure of the json if you need to
# add new data to this lookup for loop.
for i in data['items']:
    print(f"{i['title']} - {i['origin']['title']}")
