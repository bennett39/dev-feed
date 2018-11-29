import json

# TODO - still having touble with utf-8 encoding errors. Had to clean
# sample.json in order to work with it for now. Long term, need a fix.
with open("sample.json", mode="r", encoding="utf-8") as f:
    data = json.load(f)
f.close()

# Each list item will get printed as a separate line in the output file
lines = []

# Use sample-pretty.json to see the structure of the json if you need to
# add new data to this lookup for loop.
for i in data['items']:
    lines.append(f"{i['title']} - {i['origin']['title']}\n")

# TODO - come up with a naming scheme so that digests are unique
digest = open("digests/digest.md", mode="w", encoding="utf-8")
digest.writelines(lines)
digest.close()
