from BlogHandler import BlogHandler


class MainPage(BlogHandler):

    def get(self):
        self.render("index.html")
