import os
import re
import random
import hashlib
import hmac
from string import letters
import webapp2
import jinja2
from google.appengine.ext import db

from handlers.MainPage import MainPage
from handlers.NewPost import NewPost
from handlers.BlogFront import BlogFront
from handlers.Welcome import Welcome
from handlers.PostPage import PostPage
from handlers.SignUp import SignUp
from handlers.Login import Login
from handlers.Logout import Logout
from handlers.EditPost import EditPost
from handlers.DeletePost import DeletePost
from handlers.LikePost import LikePost
from handlers.AddComment import AddComment
from handlers.EditComment import EditComment
from handlers.DeleteComment import DeleteComment
from handlers.ErrorHandler import ErrorHandler

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/blog/newpost', NewPost),
                               ('/blog/?', BlogFront),
                               ('/blog/welcome/([a-zA-Z0-9]+)', Welcome),
                               ('/blog/([0-9]+)', PostPage),
                               ('/signup', SignUp),
                               ('/login', Login),
                               ('/logout', Logout),
                               ('/blog/editpost/([0-9]+)', EditPost),
                               ('/blog/deletepost/([0-9]+)', DeletePost),
                               ('/blog/likepost/([0-9]+)', LikePost),
                               ('/blog/addcomment/([0-9]+)', AddComment),
                               ('/blog/editcomment/([0-9]+)', EditComment),
                               ('/blog/deletecomment/([0-9]+)', DeleteComment),
                               ('/blog/errorhandler', ErrorHandler),
                               ],
                              debug=True)