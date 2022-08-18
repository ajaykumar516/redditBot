# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 07:39:05 2022

@author: ajayk
"""

import praw
reddit = praw.Reddit(
    client_id="gPBNj9F0er5ksssTEn27Wg",
    client_secret="BeCAOY0q0BvTE6IMScgHmkulzd_46Q",
    user_agent="<console:Bot:1.0>",
    username = 'reddit-python-bot',
    password = 'Ajay@2001'
)

subreddit = reddit.subreddit("learnpython")

text = ["reply"]

for submission in subreddit.hot(limit=10):
    #print("------------")
    #print(submission.title)
    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if " python " in comment_lower:
                 print("-----------")
                 print(comment.body)
                 comment.reply(text[0])
        
           