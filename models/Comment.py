from google.appengine.ext import db


class Comment(db.Model):
    user_id = db.StringProperty(required=True)
    blog_id = db.StringProperty(required=True)
    comment = db.StringProperty(required=True)

    @classmethod
    def render(cls, blog_id):
        posts = db.GqlQuery(
            "select * from Comment where blog_id='%s'" % str(blog_id))
        return posts
