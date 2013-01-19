"""Reddit clone using web.py
"""
import web

urls = (
    "/", "index",
    "/new", "newpost",
    "/(.*)/vote", "vote",
    "/(.*)", "post",
)
app = web.application(urls, globals())
render = web.template.render("templates/")
db = web.database(dbn="sqlite", db="reddit.db")

class index:
    def GET(self):
        posts = db.select("posts", order="votes desc")
        return render.site(render.index(posts))

class vote:
    def POST(self, pid):
        i = web.input(action="up")
        if i.action == "up":
            db.query(
                "UPDATE posts SET votes=votes+1 WHERE id=$id",
                {"id": pid})
        else:
            db.query(
                "UPDATE posts SET votes=votes-1 WHERE id=$id",
                {"id": pid})
        raise web.seeother("/")

class post:
    def GET(self, pid):
        return "Hello, post"

class newpost:
    def GET(self):
        return render.site(render.new())

    def POST(self):
        i = web.input()
        db.insert("posts", title=i.title, url=i.url)
        raise web.seeother("/")

if __name__ == "__main__":
    app.run()
