#!/usr/bin/python3
"""
    module 0-subs
    Retrieves the number of subscribers for a given subreddit
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ function to that calls the reddit api to get number of subscribers """

    API_URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    user_agent = {'User-Agent': 'QueryReddit1.0'}

    res = requests.get(API_URL, user_agent)

    if (res.status_code == 200):
        try:
            data = res.json()
            return data['data']['subscribers']

        except Exception:
            return 0
    else:
        return 0


if __name__ == "__main__":

    if len(sys.argv) == 2:
        subreddit = sys.argv[1]
        print(number_of_subscribers(subreddit))
    else:
        print("Error: Incorrect number of args:")
        print("Usage:\n\t{} <subreddit>".format(sys.argv[0]))
