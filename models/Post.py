from google.appengine.ext import db

from handlers.BlogHandler import render_str
from Comment import Comment
from LikeCount import LikeCount


class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    lastmodified = db.DateTimeProperty(auto_now=True)
    user_id = db.StringProperty(required=True)

    def get_username_from_id(self, user_id):
        key = db.Key.from_path('User', int(user_id))
        user = db.get(key)
        return user.username

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        self.likecount = LikeCount.all().filter(
            'blog_id = ', str(self.key().id())).get()
        self.comments = Comment.render(self.key().id())

        if self.likecount:
            countval = self.likecount.count

        else:
            countval = 0

        return render_str("post.html", p=self, count=countval,
                          comment=self.comments)
