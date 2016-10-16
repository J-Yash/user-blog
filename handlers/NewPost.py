from BlogHandler import BlogHandler
from models.User import User
from models.Post import Post
from models.Comment import Comment
from models.Like import Like
from models.LikeCount import LikeCount
from google.appengine.ext import db


class NewPost(BlogHandler):

    def get(self):
        if self.user:
            self.render("newpost.html")
        else:
            self.redirect("/login")

    def post(self):
        if not self.user:
            return self.redirect("/login")

        subject = self.request.get('subject')
        content = self.request.get('content')
        user_id = self.request.cookies.get('user_id').split('|')[0]

        if subject and content:
            p = Post(subject=subject, content=content, user_id=user_id)
            p.put()

            l = LikeCount(blog_id=str(p.key().id()), count=0)
            l.put()

            self.redirect('/blog/%s' % str(p.key().id()))

        else:
            error = "Both subject and content are required!"
            self.render("newpost.html", subject=subject, content=content,
                        error=error)
