#!/usr/bin/python3
"""
Module for subreddit subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """[function that queries the Reddit API
    and returns the number of subscribers for a given subreddit.]

    Args:
        subreddit ([string]): [topic of subredit]

    Returns:
        [int]: [Number of subscribers for a given topic]
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    data = requests.get(url, headers={"User-Agent": "yuyo2211"},
                        allow_redirects=False)
    if data.status_code == 200:
        return data.json().get('data').get('subscribers')
    else:
        return 0
