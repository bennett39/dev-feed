# dev-feed
Finds and sorts articles from Feedly

### To use:
1. Clone this repository
2. `pip install -r requirements.txt`
3. Get a developer API key from Feedly: https://developer.feedly.com/v3/developer/
4. Rename `.env.sample` to `.env` and add your OAuth key
5. Change the `get_stream_id()` function in `dev_feed.py` to your desired stream resource ids - https://developer.feedly.com/cloud/
6. Run `$ python dev_feed.py`. The output will save to the `digests/` folder. If the API encounters an error it will print to the console.

### Command line options:
The command line structure is...

```bash
$ python dev_feed.py [feed id] <optional # of articles to return>
```

So, `$ python dev_feed.py dev 100` will output the top `100` articles from the `dev` stream
