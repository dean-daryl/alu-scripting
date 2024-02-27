#!/usr/bin/python3
import requests

def hot_ten(subbreddit):
    """function to get the top ten posts for a subbreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subbreddit)

    try:
        response = requests.get(url,verify=False)
        posts = response.json().get("data").get("children")
        [print(post.get('data').get('title')) for post in posts]
    except Exception:
        print(None)
