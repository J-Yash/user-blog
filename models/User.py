from google.appengine.ext import db

class User(db.Model):
    username = db.StringProperty(required = True)
    password = db.StringProperty(required = True)
    email = db.StringProperty(required = True)

    @classmethod
    def getname(cls, name):
        u = User.all().filter('username =', name).get()
        return u

    @classmethod
    def get_using_id(cls, user_id):
        return cls.get_by_id(user_id)