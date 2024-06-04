#!/usr/bin/python3
"""
This script defines a function to list first 10 hot posts for a subreddit
"""


def top_ten(subreddit):
    """
    Prints titles of first 10 hot posts for given subreddit
    using the reddit API

    Example:
    >>> top_ten(programming)
    How a 64k intro is made
    HTTPS on Stack Overflow: The End of a Long Road
    ...

    Args:
    subreddit (str): The subreddit to be searched for

    Returns:
    int: 1 valid subreddit or 0 for invalid subreddit

    NOTE:
    The function prints the list of hot posts internally
    """
    import requests

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "Fake-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        counter = 0
        for post in response.json().get('data').get('children'):
            print(post.get('data').get('title'))
            counter += 1
            if counter >= 10:
                break
        return_status = 1
    else:
        print("None")
        return_status = 0

    return return_status
