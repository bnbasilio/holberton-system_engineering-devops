#!/usr/bin/python3
""" 0. How many subs? """
import requests


def number_of_subscribers(subreddit):
    res = requests.get('https://reddit.com/r/{}/about.json'.format(subreddit),
                       headers={'User-Agent': 'bnbasilio-app'})
    try:
        jsonResponse = res.json()
        return jsonResponse["data"]["subscribers"]
    except:
        return 0
