from BlogHandler import BlogHandler
from models.User import User
from models.Post import Post
from models.Comment import Comment
from models.Like import Like
from models.LikeCount import LikeCount
from google.appengine.ext import db


class LikePost(BlogHandler):

    def get(self, blog_id):
        if not self.user:
            self.redirect("/login")

        user_id = self.request.cookies.get('user_id').split('|')[0]

        value = Like.all().filter('user_id = ', user_id).filter('blog_id = ',
                                                                blog_id).get()

        if value:
            value.delete()

            likecount = LikeCount.all().filter('blog_id = ', blog_id).get()
            likecount.count = likecount.count - 1
            likecount.put()

            self.redirect("/blog/")

        else:

            key = db.Key.from_path('Post', int(blog_id))
            post = db.get(key)

            if post.user_id == user_id:
                self.redirect("/blog/errorhandler")

            else:
                l = Like(user_id=user_id, blog_id=blog_id, status="liked")
                l.put()

                likecount = LikeCount.all().filter('blog_id = ', blog_id).get()
                likecount.count = likecount.count + 1
                likecount.put()

                self.redirect("/blog/")
