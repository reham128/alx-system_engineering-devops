#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """To count all words"""
    if counts is None:
        counts = {}
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {'User-Agent':
               'python:subreddit.count_words:v1.0 (by /u/reham_saeed)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    if title.count(word.lower()) > 0:
                        if word.lower() not in counts:
                            counts[word.lower()] = 1
                        else:
                            counts[word.lower()] += 1
            after = data['data']['after']
            if after is not None:
                return count_words(subreddit, word_list, after, counts)
            else:
                sorted_counts = sorted(counts.items(),
                                       key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        else:
            return
    except requests.RequestException:
        return
