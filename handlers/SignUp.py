from BlogHandler import BlogHandler
import validate
from models.User import User
from models.Post import Post
from models.Comment import Comment
from models.Like import Like
from models.LikeCount import LikeCount


class SignUp(BlogHandler):

    def get(self):
        self.render("signup.html")

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verifypassword = self.request.get('verifypassword')
        email = self.request.get('email')
        flag = False
        errorusername = ""
        errorpassword = ""
        errorverpassword = ""
        erroremail = ""

        if username and password and verifypassword and email:

            if not validate.valid_username(username):
                errorusername = "Username is not valid!"
                flag = True

            elif not validate.valid_password(password):
                errorpassword = "Password is not valid!"
                flag = True
            elif password != verifypassword:
                errorverpassword = "Passwords do not match!"
                flag = True
            elif not validate.valid_email(email):
                erroremail = "E-mail is not valid!"
                flag = True
            else:
                name = User.getname(username)

                if not name:
                    pwd = self.make_secure_password(username, password)
                    u = User(username=username, password=pwd,
                             email=email)
                    u.put()
                    self.login(u)
                    self.redirect("/blog/welcome/%s" % username)
                else:
                    errorusername = "User already exists!"
                    flag = True
            if flag == True:
                self.render("signup.html", username=username, email=email,
                    errorusername=errorusername, errorpassword=errorpassword,
                    errorverpassword=errorverpassword, erroremail=erroremail)

        else:
            error = "All fields are mandatory!"
            self.render("signup.html", username=username, email=email,
                        error=error)
