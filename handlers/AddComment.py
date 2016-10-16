from BlogHandler import BlogHandler
from models.User import User
from models.Post import Post
from models.Comment import Comment
from models.Like import Like
from models.LikeCount import LikeCount
from google.appengine.ext import db


class AddComment(BlogHandler):

    def post(self, blog_id):
        if not self.user:
            self.redirect("/login")

        user_id = self.request.cookies.get('user_id').split('|')[0]
        commentstr = self.request.get('comment')
        com = Comment(user_id=user_id, blog_id=blog_id, comment=commentstr)
        com.put()

        self.redirect("/blog/")
