from BlogHandler import BlogHandler
from models.User import User
from models.Post import Post
from models.Comment import Comment
from models.Like import Like
from models.LikeCount import LikeCount
from google.appengine.ext import db


class DeleteComment(BlogHandler):

    def get(self, comment_id):
        if not self.user:
            self.redirect("/login")

        user_id = self.request.cookies.get('user_id').split('|')[0]
        key = db.Key.from_path('Comment', int(comment_id))
        comment = db.get(key)

        if comment.user_id == user_id:
            comment.delete()
            self.redirect("/blog/")

        else:
            self.redirect("/blog/errorhandler")
