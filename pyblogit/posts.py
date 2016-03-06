"""
pyblogit.posts
~~~~~~~~~~~~~~

This module contains the data model to represent blog posts and methods
to manipulate it.
"""

class post(object):
    """The post data model"""

    def __init__(self, post_id, title, url, author, content, images, labels,
            status):
        self._post_id = post_id
        self._title = title
        self._url = url
        self._author = author
        self._content = content
        self._images = images
        self._labels = labels

    @property
    def post_id(self):
        return self._post_id

    @property
    def title(self):
        return self._title

    @property
    def url(self):
        return self._url

    @property
    def author(self):
        return self._author

    @property
    def content(self):
        return self._content

    @property
    def images(self):
        return self._images

    @property
    def labels(self):
        return self._labels

