from BlogHandler import BlogHandler
from models.User import User
from models.Post import Post
from models.Comment import Comment
from models.Like import Like
from models.LikeCount import LikeCount
from google.appengine.ext import db


class ErrorHandler(BlogHandler):

    def get(self):
        error = "Oops! Looks like you don't have the permission to do that!!!"
        self.render("error.html", error=error)
