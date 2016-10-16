from BlogHandler import BlogHandler
from models.User import User
from models.Post import Post
from models.Comment import Comment
from models.Like import Like
from models.LikeCount import LikeCount
from google.appengine.ext import db


class EditPost(BlogHandler):

    def get(self, blog_id):
        if not self.user:
            self.redirect("/login")
        else:
            user_id = self.request.cookies.get('user_id').split('|')[0]
            key = db.Key.from_path('Post', int(blog_id))
            post = db.get(key)

            if post.user_id == user_id:
                self.render("editpost.html", post=post)

            else:
                self.redirect("/blog")

    def post(self, blog_id):
        if not self.user:
            self.redirect("/login")

        else:
            user_id = self.request.cookies.get('user_id').split('|')[0]
            key = db.Key.from_path('Post', int(blog_id))
            post = db.get(key)

            if post.user_id == user_id:
                subject = self.request.get('subject')
                content = self.request.get('content')
                if subject and content:
                    post.subject = subject
                    post.content = content
                    post.put()
                    self.redirect('/blog/%s' % str(post.key().id()))

                else:
                    error = "Both fields are required!"
                    self.render("editpost.html", subject=subject,
                        content=content, error=error)

            else:
                self.redirect("/blog")
