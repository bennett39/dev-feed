import requests

from secrets import api_key # Add your own api_key to secrets.py


def main():
    # Main Feedly API. Use sandbox.feedly.com for testing.
    # Change endpoint to access other feeds/articles/users/etc
    # Documentation: https://developer.feedly.com/
    endpoint = "https://cloud.feedly.com/v3/streams/contents"

    # Dictionary that feeds into requests module to create URL
    # e.g. - "/v3/streams/contents?streamId=feed%2Fhttp..."
    # Documentation:
    # https://developer.feedly.com/v3/streams/#get-the-content-of-a-stream
    payload = {
        # Resource ID for stream you want to access
        "streamId": ("user/c04622d3-e092-4537-b5d5-a326858ffe1d/"
                    "category/Tech - Development"),

        # Optional settings
        "unreadOnly": True,
        "count": 5
    }

    r = requests.get(endpoint, headers=api_key, params=payload)
    create_digest(r)


def create_digest(r):
    """
    Convert request response JSON to a readable markdown file
    """
    
    if r.status_code == 200:
        data = r.json()
        
        # Each list item will get printed as a separate line in the output file
        lines = []

        # Use sample-pretty.json to see the structure of the json if you need to
        # add new data to this lookup for loop.
        for i in data['items']:
            lines.append(f"[{i['title']}]({i['originId']}) \
                        \n{i['origin']['title']}\n\n")

        # TODO - come up with a naming scheme so that digests are unique
        with open("digests/digest.md", mode="w", encoding="utf-8",
                errors="surrogateescape") as f:
            f.writelines(lines)

        f.close()

        return print("Success")

    else:
        return print(f"ERROR: {r.status_code}")


if __name__ == "__main__":
    main()
