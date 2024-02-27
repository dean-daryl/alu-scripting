#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """function that gets amount of subscribers on a reddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    try:
        resp = requests.get(url,verify=False)
        return resp.json().get("data").get("subscribers")
    except Exception:
        return "Oops something went wrong",Exception
