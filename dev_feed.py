import requests
import sys

from datetime import datetime
from secrets import api_key

def main():
    endpoint = "https://cloud.feedly.com/v3/streams/contents"
    payload = {
        "streamId": get_stream_id(sys.argv),
        "unreadOnly": True,
        "count": get_count(sys.argv)
    }
    response = requests.get(endpoint, headers=api_key, params=payload)
    create_digest(response)


def create_digest(r):
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
        now = datetime.now()
        file_name = f"digests/{now.strftime('%Y_%m_%d_%H%M')}-{sys.argv[1]}.md"
        with open(file_name, mode="w", encoding="utf-8", errors="surrogateescape") as f:
            f.writelines(lines)
        print(f"Digest created at {file_name}")
    else:
        return print(f"ERROR: {r.status_code}")


def get_count(argv):
    """ Get article count from the command line. Default is 200 """
    try:
        if int(argv[2]) <= 1000:
            return int(argv[2])
        else:
            raise IndexError
    except IndexError:
        return 200


def get_stream_id(argv):
    """
    Get the stream id based on command line prompt.
    Valid prompts: "dev" or "news"
    """
    dev_id = ("user/c04622d3-e092-4537-b5d5-a326858ffe1d/category/Tech - Development")
    news_id =  ("user/c04622d3-e092-4537-b5d5-a326858ffe1d/category/Management")
    try:
        if argv[1] == "dev":
            return dev_id
        elif argv[1] == "news":
            return news_id
        else:
            raise IndexError
    except IndexError:
        return dev_id


if __name__ == "__main__":
    main()
