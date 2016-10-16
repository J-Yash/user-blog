from google.appengine.ext import db


class LikeCount(db.Model):
    blog_id = db.StringProperty(required=True)
    count = db.IntegerProperty(required=True)
