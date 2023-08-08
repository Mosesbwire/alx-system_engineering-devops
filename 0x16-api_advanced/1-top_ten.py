#!/usr/bin/python3

"""
    module 1-top_ten:
    Retrieves top 10 hottest post in a subreddit
"""

import requests
import sys


def top_ten(subreddit):
    """ queries the api endpoint returns top 10 posts """

    API_URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    user_agent = {'User-Agent': 'Queryreddit1.0'}

    res = requests.get(API_URL, headers=user_agent, allow_redirects=False)

    if res.status_code == 200:
        try:
            data = res.json()
            posts = data['data']['children']
            for post in posts[:10]:
                print(post['data']['title'])
        except Exception:
            print(None)
    else:
        print(None)


if __name__ == "__main__":

    if len(sys.argv) == 2:
        top_ten(sys.argv[1])
    else:
        print("Error: Wrong number of arguments passed")
        print("Usage:\n\t{} <subreddit>".format(sys.argv[0]))
