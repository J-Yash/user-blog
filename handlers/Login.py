from BlogHandler import BlogHandler
from models.User import User
from models.Post import Post
from models.Comment import Comment
from models.Like import Like
from models.LikeCount import LikeCount


class Login(BlogHandler):

    def get(self):
        self.render("login.html")

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        flag = False
        errorusername = ""
        errorpassword = ""

        if not username:
            errorusername = "Username required!"
            flag = True
        else:
            u = User.getname(username)
            if not u:
                errorusername = "Username is incorrect!"
                flag = True
            else:
                if not password:
                    errorpassword = "Password required!"
                    flag = True
                else:
                    value = u.password
                    saltvalue = value.split(",")[1]
                    pwd = value.split(",")[0]
                    word = username + password + saltvalue
                    if pwd != self.make_secure_password(username,
                                password, saltvalue).split(",")[0]:
                        flag = True
                        errorpassword = "Password is Invalid!"
                    else:
                        self.login(u)
                        self.redirect("/blog/welcome/%s" % username)

        if flag == True:
            self.render("login.html", errorusername=errorusername,
                        errorpassword=errorpassword, username=username)
