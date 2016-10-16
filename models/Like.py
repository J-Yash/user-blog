from google.appengine.ext import db


class Like(db.Model):
    user_id = db.StringProperty(required=True)
    blog_id = db.StringProperty(required=True)
    status = db.StringProperty(required=True)
