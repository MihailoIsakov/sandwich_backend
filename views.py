from datetime import datetime

from manage import app
from flask.views import request
from flask import jsonify

from sandwich_backend import comments, reactions


@app.route('/comment')
def upsert_comment():
    userid = request.args.get('userid')                 # Goes in the user reaction
    comment_id = request.args.get('id')                 # Goes in the comment, used as ID
    link = request.args.get('link')                     # Goes in the comment, should be updated to the article page if found
    author = request.args.get('author')                 # Goes in the comment, used as ID
    parent_author = request.args.get('parent_author')   # Goes in the comment
    comment = request.args.get('comment')               # Goes in the comment
    vote_count = request.args.get('vote_count')         # Goes in the comment
    upvotes = request.args.get('upvotes')               # Goes in the comment
    downvotes = request.args.get('downvotes')           # Goes in the comment
    bot = request.args.get('bot')                       # Goes in the user reaction 

    comments.update(
        {
            'comment_id': comment_id, 
            'author': author,
        },
        {'$set':
            {
                'comment_id': comment_id, 
                'link': link,
                'comment': comment, 
                'author': author,
                'parent_author': parent_author,
                'vote_count': vote_count,
                'upvotes': upvotes,
                'downvotes': downvotes
            }
        },
        upsert=True
    )

    reactions.update(
        {
            'comment_id': comment_id,
            'userid': userid
        },
        {
            '$set': {
                'bot': bot,
                'time': datetime.now()
            }
        },
        upsert = True
    )

    bot_count = reactions.find(
        {'comment_id': comment_id, 'bot': 'true'}).count()

    not_count = reactions.find(
        {'comment_id': comment_id, 'bot': 'false'}).count()

    result = jsonify({'bot_count': bot_count, 'not_count': not_count})
    return result
