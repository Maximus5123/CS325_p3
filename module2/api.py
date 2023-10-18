# modules/reddit_api.py
import praw

def get_reddit_post(url, client_id, client_secret, user_agent):
    reddit = praw.Reddit(client_id=client_id,
                        client_secret=client_secret,
                        user_agent=user_agent)
    post = reddit.submission(url=url)
    return post
