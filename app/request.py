import urllib.request,json
from models.quote import Quote
from models.post import Post
from models.comment import Comment

def get_quote():
    '''
    Function that retrieves quotes
    '''
    quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(quote_url) as url:
        quote_data = url.read()
        quote_response = json.loads(quote_data)

    return quote_response

def post_comment_count(catid):
    '''
    Function that gets post comments
    '''
    posts = Post.get_posts(catid)
    comments = Comment.get_comments()

    post_comments = []

    if posts:
        for post in posts:
            post_id = post.id
            count = 0
            if comments:
                for comment in comments:
                    if comment.post_id == post_id:
                        count +=1
            
            post_comments.append({"post_id":post.id, "num_comments":count})
            count = 0
            
    return post_comments

def individual_post_comment_count(pid):
    '''
    Function that gets post comments
    '''
    post = Post.query.filter_by(id=pid).first()
    comments = Comment.get_comments()

    post_comments = []

    if post:
        post_id = post.id
        count = 0
        if comments:
            for comment in comments:
                if comment.post_id == post_id:
                    count +=1
        
        post_comments.append({"post_id":post.id, "num_comments":count})
            
    return post_comments