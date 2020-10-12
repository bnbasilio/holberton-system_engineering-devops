#!/usr/bin/python3
""" 2. Recurse it! """
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    returns a list containing the titles of all hot articles
    for a given subreddit
    """
    r = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'.
                     format(subreddit, after),
                     headers={'User-Agent': 'custom'},
                     allow_redirects=False)
    if r.status_code != 200:
        return None
    if after is None:
        return hot_list
    for thread in r.json().get('data').get('children'):
        hot_list += [thread.get('data').get('title')]
    after = r.json().get('data').get('after')
    recurse(subreddit, hot_list, after)
    return hot_list
