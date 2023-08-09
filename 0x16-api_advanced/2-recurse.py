#!/usr/bin/python3

"""
    module 2-recurse:
    queries a subreddit returning all hot topics
"""
import requests


def recurse(subreddit, hot_list=[], count=0, next_page=None):
    """query reddit api returns list containing titles of all hot articles"""

    headers = {
        "User-Agent": "QueryReddit1.0"
    }
    API_URL = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {"limit": 50, "next_page": next_page, "count": count}
    res = requests.get(API_URL, headers=headers,
                       params=params, allow_redirects=False)
    if res.status_code != 200:
        return None
    data = res.json().get("data")
    next_page = data.get("next_page")
    count += data.get("dist")
    children = data.get("children")
    for child in children:
        title = child.get("data").get("title")
        hot_list.append(title)
    if next_page is not None:
        return recurse(subreddit, hot_list, count, next_page)
    return hot_list
