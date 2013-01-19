"""Helloworld app with web.py

How to run:

    $ python hello3.py
    http://0.0.0.0:8080
    ...

URLs to try:

    http://0.0.0.0:8080/
    http://0.0.0.0:8080/anything
"""
import web

urls = (
    "/(.*)", "hello"
)

app = web.application(urls, globals())

render = web.template.render("templates/")

class hello:
    def GET(self, name):
        name = name or "world"
        return render.hello(name)

if __name__ == "__main__":
    app.run()
