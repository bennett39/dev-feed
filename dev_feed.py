import requests
import sys

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
        "streamId": get_stream_id(sys.argv),

        # Optional settings
        "unreadOnly": True,
        "count": get_count(sys.argv) 
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

        file_name = get_file_name(sys.argv)
        
        # TODO - come up with a naming scheme so that digests are unique
        with open(file_name, mode="w", encoding="utf-8",
                errors="surrogateescape") as f:
            f.writelines(lines)

        f.close()

        return print("Success")

    else:
        return print(f"ERROR: {r.status_code}")


def get_count(argv):
    """
    Get article retrieval count from the command line. Default if
    unspecified is 5
    """
    try:
        if int(argv[3]) <= 1000:
            return int(argv[3])
        else:
            return 5

    except IndexError:
        return 5


def get_file_name(argv):
    """
    Get file name from the command line. Default if unspecified is
    "digest.md". Files automatically save to the digests/ folder.
    """

    try:
        return f"digests/{argv[2]}.md"

    except IndexError:
        return "digests/digest.md"


def get_stream_id(argv):
    """
    Get the stream id based on command line prompt. 
    Valid prompts: "dev" or "news"
    """

    dev_id = ("user/c04622d3-e092-4537-b5d5-a326858ffe1d/"
              "category/Tech - Development")
    news_id =  ("user/c04622d3-e092-4537-b5d5-a326858ffe1d/"
                "category/Management")

    if argv[1] == "dev":
        return dev_id
    elif argv[1] == "news":
        return news_id
    else:
        return dev_id


if __name__ == "__main__":
    main()
