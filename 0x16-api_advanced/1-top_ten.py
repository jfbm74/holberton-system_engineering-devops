#!/usr/bin/python3
"""[Module API - Reddit Top Ten]
"""


import requests


def top_ten(subreddit):
    """[ prints the titles of the first 10 hot posts
    listed for a given subreddit.]

    Args:
        subreddit ([string]): [subs.py:21:3]
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    data = requests.get(url, headers={"User-Agent": "yuyo2211"},
                        allow_redirects=False)

    if data.status_code == 200:
        for subredit in data.json()['data']['children']:
            print(subredit['data']['title'])
    else:
        print(None)
