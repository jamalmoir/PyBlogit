"""
pyblogit.blogs
~~~~~~~~~~~~~~~~~~~

This module contains the data model to represent a blog and methods to
manipulate it.
"""

class blog(object):
    """The blog data model"""

    def __init__(self, blog_id, name, url, desc, posts, pages):
        self._blog_id = blog_id
        self._name = name
        self._url = url
        self._desc = desc
        self._posts = posts
        self._pages = pages

    @property
    def blog_id(self):
        return self._blog_id

    @property
    def name(self):
        return self._name

    @property
    def url(self):
        return self._url

    @property
    def desc(self):
        return self._desc

    @property
    def posts(self):
        return self._posts

    @property
    delf pages(self):
        return self._pages
