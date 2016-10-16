import os
import re
import random
import hashlib
import hmac
from string import letters

import webapp2
import jinja2

from google.appengine.ext import db

from models.User import User
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

# Some helper functions to make a few recurring things easier to use.
class BlogHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def set_secure_cookie(self, name, value):
        securevalue = value + "|" + hmac.new('qwerty', value).hexdigest()
        self.response.headers.add_header('Set-Cookie',
                                         '%s=%s; Path=/' % (name, securevalue))

    def make_secure_password(self, username, password, salt=None):
        if not salt:
            salt = ''.join(random.choice(letters) for x in xrange(5))

        securepassword = hashlib.sha256(username + password + salt).hexdigest()
        return "%s,%s" % (securepassword, salt)

    def login(self, user):
        self.set_secure_cookie("user_id", str(user.key().id()))

    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        self.user = None
        cookie = self.request.cookies.get('user_id')
        if cookie:
            user_id = cookie.split('|')[0]
            secval = cookie.split('|')[1]
            if hmac.new('qwerty', user_id).hexdigest() != secval:
                self.redirect("/login")
            else:
                self.user = User.get_using_id(int(user_id))
