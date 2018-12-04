import requests

from secrets import api_key # Add your own api_key to secrets.py


def main():
    r = get_user_stream(api_key)
    create_digest(r)


def get_user_stream(api_key):
    """
    Fetches user article stream from Feedly API. Authentication
    required
    """
    
    # Main Feedly API. Use sandbox.feedly.com for testing.
    # Documentation: https://developer.feedly.com/
    url_base = "https://cloud.feedly.com/v3/streams/contents"

    # Resource ID for the stream you want to access
    # Documentation: https://developer.feedly.com/cloud/
    user_streamId = ("user/c04622d3-e092-4537-b5d5-a326858ffe1d/"
                    "category/Tech - Development")

    # Dictionary that feeds into requests module to create URL
    # e.g. - "/v3/streams/contents?streamId=feed%2Fhttp..."
    # Optional: count (default 20), unreadOnly (boolean)
    # Documentation:
    # https://developer.feedly.com/v3/streams/#get-the-content-of-a-stream
    payload = {
        "streamId": user_streamId,
        "unreadOnly": True,
        "count": 5
    }

    # Get API response using requests module - requests must be installed
    return requests.get(url_base, headers=api_key, params=payload)


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
