# run.py
import os
import sys
from module2.api import get_reddit_post
from module1.processing import retrieve_comments, save_comments_to_file

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 run.py URL")
        sys.exit(1)
    
    post_url = sys.argv[1]
    client_id = '4iuS6Vi6nMblW8NXKFudrQ'
    client_secret = '4kkKBJ4_rkD4Bh6ijoiAqQd1MPoTYQ'
    user_agent = 'Maximus<red>'
    
    post = get_reddit_post(post_url, client_id, client_secret, user_agent)
    comments = retrieve_comments(post)
    
    output_dir = os.path.join("Data", "processed")
    output_file = os.path.join(output_dir, "processed_data.txt")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    save_comments_to_file(comments, output_file)
    print("Comments saved to", output_file)
