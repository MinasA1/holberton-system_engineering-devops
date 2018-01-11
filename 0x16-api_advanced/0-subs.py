#!/usr/bin/python3
"""number_of_subscribers"""
from requests import get


def number_of_subscribers(subreddit):
    """reddit API"""
    if type(subreddit) is not str:
        return 0
    api = "https://www.reddit.com/r/{}/about/.json".format(subreddit)
    header = {'user-agent': 'MinasA1'}
    r = get(api, headers=header, allow_redirects=False)
    if r.status_code is 200:
        return r.json()['data']['subscribers']
    return 0
