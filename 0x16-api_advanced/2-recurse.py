#!/usr/bin/python3
"""recurse reddit API"""
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """query hot articles"""
    api = 'https://www.reddit.com/r/{}/hot.json?limit'.format(subreddit)
    header = {'User-Agent': 'Chrome'}
    if after:
        api = '{}&after={}'.format(api, after)
    r = get(api, headers=header)
    if r.status_code > 200:
        return None
    r = r.json()
    child = r['data']['children']
    after = r['data']['after']
    for i in child:
        title = i['data']['title']
        hot_list.append(title)
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
