def retrieve_comments(post):
    comment_list = []
    # Access the comments
    post.comments.replace_more(limit=5)  # This loads all the comments
    comments = post.comments.list()
    
    # Append comments to the comment_list
    for comment in comments:
        output = comment.body
        comment_list.append(output)
    
    return comment_list

def save_comments_to_file(comment_list, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for comment in comment_list:
            file.write(f'{comment}\n')
