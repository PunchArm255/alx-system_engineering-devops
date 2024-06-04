#!/usr/bin/python3
"""
This script defines a function to list all hot posts for a subreddit
using recursion
"""


def recurse(subreddit, hot_list=[], after='start'):
    """
    Lists titles of all hot posts for given subreddit recursively
    using the reddit API

    Example:
    >>> recurse(programming)
    ["How a 64k intro is made", "Birth of BASIC",
    ...]

    Args:
    subreddit (str): The subreddit to be searched for
    hot_list (list): List to hold posts' titles to be returned
    after (str): Index to keep track of remaining pages `NOT TO BE CHANGED`

    Returns:
    list: List of hot posts' titles
    """
    import requests

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "Fake-Agent"}
    if after != 'start':
        url += "?after={}".format(after)

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    for post in response.json().get('data').get('children'):
        hot_list.append(post.get('data').get('title'))

    after = response.json().get('data').get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
