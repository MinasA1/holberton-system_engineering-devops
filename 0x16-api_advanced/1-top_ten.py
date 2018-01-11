#!/usr/bin/python3
"""top ten"""
from requests import get


def top_ten(subreddit):
    """reddit API"""
    if type(subreddit) is not str:
        return 0
    api = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {'user-agent': 'chrome'}
    r = get(api, headers=header, allow_redirects=False)
    if r.status_code is 200:
        js = r.json()['data']['children']
        return '\n'.join([js[i]['data']['title']for i in range(10)])
    return None
