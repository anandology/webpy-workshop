"""Helloworld app with web.py

How to run:

    $ python hello1.py
    http://0.0.0.0:8080
    ...

URLs to try:

    http://0.0.0.0:8080/
    http://0.0.0.0:8080/anything
"""
import web

# specify the URL patterns
# The first one is the URL pattern and second one is the name of the class
# The URL pattern can be a regular expression. What ever is matched by () will
# be passed to the method called.
urls = (
    "/(.*)", "hello"
)

# create an app using the urls. 
# We need to pass globals() so that web.py can get the class object from class
# name.
app = web.application(urls, globals())

# The class to handle the request.
# GET method is called for GET request and POST method is called for POST
# request and so on.
class hello:
    # Whatever is matched by the group in the URL pattern will be passsed as
    # argument to this function.
    def GET(self, name):
        name = name or "world"
        return "Hello, %s!\n" % name

if __name__ == "__main__":
    app.run()
