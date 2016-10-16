from BlogHandler import BlogHandler
from models.User import User
from models.Post import Post
from models.Comment import Comment
from models.Like import Like
from models.LikeCount import LikeCount


class Welcome(BlogHandler):

    def get(self, username):

        self.render("welcome.html", username=username)
