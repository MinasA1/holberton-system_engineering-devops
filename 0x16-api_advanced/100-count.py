#!/usr/bin/python3
"""recurse reddit API"""
from requests import get


def count_words(subreddit, word_list, after=None, counts={}):
    """query hot articles"""
    api = 'https://www.reddit.com/r/{}/hot.json?limit'.format(subreddit)
    header = {'User-Agent': 'Chrome'}
    if after:
        api = '{}&after={}'.format(api, after)
    r = get(api, headers=header, allow_redirects=False)
    if r.status_code > 200:
        return None
    r = r.json()
    child = r['data']['children']
    after = r['data']['after']
    word_list = list(set(word_list))
    for i in word_list:
        if not counts.get(i):
            counts[i] = 0
    for i in child:
        title = i['data']['title']
        title = title.lower()
        title = title.split()
        for word in word_list:
            for w in title:
                if w == word.lower():
                    counts[word] += 1
    if after:
        return count_words(subreddit, word_list, after, counts)
    for k, v in sorted(counts.items(), key=lambda item: (item[1], item[0]),
                       reverse=True):
        if v is not 0:
            print('{}: {}'.format(k, v))
