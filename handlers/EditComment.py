from BlogHandler import BlogHandler
from models.User import User
from models.Post import Post
from models.Comment import Comment
from models.Like import Like
from models.LikeCount import LikeCount
from google.appengine.ext import db


class EditComment(BlogHandler):

    def get(self, comment_id):
        if not self.user:
            self.redirect("/login")
        else:
            user_id = self.request.cookies.get('user_id').split('|')[0]
            key = db.Key.from_path('Comment', int(comment_id))
            comment = db.get(key)

            if comment.user_id == user_id:
                self.render("editcomment.html", comment=comment)

            else:

                self.redirect("/blog/errorhandler")

    def post(self, comment_id):
        if not self.user:
            self.redirect("/login")

        else:
            user_id = self.request.cookies.get('user_id').split('|')[0]
            key = db.Key.from_path('Comment', int(comment_id))
            comment = db.get(key)

            if comment.user_id == user_id:
                subject = self.request.get('comment')
                if subject:
                    comment.comment = subject
                    comment.put()
                    self.redirect('/blog/')

                else:
                    error = "Comment is required!"
                    self.render("editpost.html", comment=subject, error=error)

            else:
                self.redirect("/blog/errorhandler")
