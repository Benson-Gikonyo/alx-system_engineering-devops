#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers """


import requests


def number_of_subscribers(subreddit):
    """ return num subscribers in a subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0

    response = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': "linux:0x16.api.advanced:v1.0.0 (by /u/ben_g)"}).json()
    results = response.get("data", {}).get("subscribers", 0)

    return results
