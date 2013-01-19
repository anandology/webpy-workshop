"""Helloworld app with web.py

How to run:

    $ python hello0.py
    http://0.0.0.0:8080
    ...

URLs to try:

    http://0.0.0.0:8080/
"""
import web

# specify the URL patterns
# The first one is the URL and second one is the name of the class
urls = (
    "/", "hello"
)

# create an app using the urls. 
# We need to pass globals() so that web.py can get the class object from class
# name.
app = web.application(urls, globals())

# The class to handle the request.
# GET method is called for GET request and POST method is called for POST
# request and so on.
class hello:
    def GET(self):
        return "Hello, world!\n"

if __name__ == "__main__":
    app.run()
