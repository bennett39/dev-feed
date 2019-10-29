import os
import requests
import sys

from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


def main():
    try:
        stream_arg, count_arg = sys.argv[1], sys.argv[2]
    except IndexError:
        stream_arg, count_arg = "dev", 200

    endpoint = "https://cloud.feedly.com/v3/streams/contents"
    payload = {
        "streamId": get_stream_id(stream_arg),
        "unreadOnly": True,
        "count": get_count(count_arg),
    }
    headers = {
        'Authorization': f'OAuth {os.getenv("API_KEY")}'
    }

    response = requests.get(endpoint, headers=headers, params=payload)

    now = datetime.now()
    file_name = f"digests/{now.strftime('%Y%m%d_%H%M')}-{stream_arg}.md"

    create_digest(response, file_name)


def create_digest(r, file_name):
    """ Convert request response JSON to a readable markdown file """
    if r.ok:
        data = r.json()
        lines = []
        for i in data['items']:
            try:
                link = i['canonicalUrl']
            except KeyError:
                link = i['originId']
            try:
                lines.append(f"[{i['title']}]({link})\n" \
                            f"{i['origin']['title']}\n\n")
            except KeyError:
                lines.append(f"Key error parsing entry.\n\n")
        with open(file_name, mode="w", encoding="utf-8", errors="surrogateescape") as f:
            f.writelines(lines)
        print(f"Digest created at {file_name}")
    else:
        return print(f"ERROR: {r.status_code}")


def get_count(count_arg):
    """ Get article count from the command line. """
    COUNT_DEFAULT=200
    try:
        if int(count_arg) <= 1000:
            return int(count_arg)
        print("Count must be less than 1,000. Defaulting to 200...")
        return COUNT_DEFAULT
    except TypeError:
        return COUNT_DEFAULT


def get_stream_id(stream):
    """
    Get the stream id based on command line prompt.
    Valid prompts: "dev" or "news"
    """
    DEFAULT_STREAM = "dev"
    ids = {
        "dev": "user/c04622d3-e092-4537-b5d5-a326858ffe1d/category/Tech - Development",
        "news": "user/c04622d3-e092-4537-b5d5-a326858ffe1d/category/Management"
    }
    try:
        return ids[stream]
    except KeyError:
        print(f"Invalid stream specified: {stream}. Options are {ids.keys()}\n========")
        print(f"Defaulting to {DEFAULT_STREAM}")
        return ids[DEFAULT_STREAM]


if __name__ == "__main__":
    main()
