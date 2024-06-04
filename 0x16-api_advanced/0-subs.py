#!/usr/bin/python3
"""
This scripts defines func to get total soobs of subreddit
"""


def number_of_subscribers(subreddit):
    """
    Returns total number of subscribers of a given subreddit
    using the reddit API

    Example:
    >>> number_of_subscribers(programming)
    756024

    Args:
    subreddit (str): The subreddit to be searched for

    Returns:
    int: Total number of subscribers of the given subreddit
         0 for invalid subreddit
    """
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"user-agent": "Fake-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        total_subscribers = 0
    else:
        total_subscribers = response.json().get('data').get('subscribers')

    return total_subscribers
