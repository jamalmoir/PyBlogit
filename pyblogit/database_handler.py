"""
pyblogit.database_handler
~~~~~~~~~~~~~~~~~~~~~~~~~

This module handles the connection and manipulation of the local database.
"""
import sqlite3
import time


def get_connection(blog_id):
    """Connects to a local sqlite database

    Parameters:
    ~~~~~~~~~~~
    blog_id : id
        The id of the blog whose database to connect to.

    Returns:
    ~~~~~~~~
    conn : sqlite3.Connection
        A sqlite3 Connection object, connected to a local database.
    """
    blog_id = str(blog_id)
    conn = sqlite3.connect(''.join((blog_id, '.db')))

    return conn


def add_blog(blog_id, name):
    """Adds a new blog to the local blogs database and
    creates a new database for the blog.

    Parameters:
    ~~~~~~~~~~~
    blog_id : int
        The id of the blog to add.
    name : str
        The name of the blog to add.
    """
    with get_connection('blogs') as conn:
        c = conn.cursor()

        # Check if blogs table exists, if it doesn't create it.
        exists = c.execute('SELECT name FROM sqlite_master WHERE type="table"'
                           'AND name="blogs"').fetchone()

        if not exists:
            c.execute('CREATE TABLE blogs(blog_id INT PRIMARY KEY,'
                      'blog_name TEXT)')

        c.execute('INSERT INTO blogs VALUES (?, ?)', (blog_id, name))

    with get_connection(blog_id) as conn:
        c = conn.cursor()

        # Create table to store posts in new blog's database.
        c.execute('CREATE TABLE posts(post_id INT PRIMARY KEY, title TEXT,'
                  'url TEXT, status TEXT, content TEXT, updated INT)')


def get_blogs():
    """Returns all stored blogs.

    Returns:
    ~~~~~~~~
    blogs : list
        A list of tuples representing a blog. The tuples are
        in the form (blog_id, name).
    """
    with get_connection('blogs') as conn:
        c = conn.cursor()

        # Check if blogs table exists, if it doesn't create it.
        exists = c.execute('SELECT name FROM sqlite_master WHERE type="table"'
                           'AND name="blogs"').fetchone()

        if not exists:
            c.execute('CREATE TABLE blogs(blog_id INT PRIMARY KEY,'
                      'blog_name TEXT)')


        c.execute('SELECT * FROM blogs')
        blogs = c.fetchall()

    return blogs


def add_post(blog_id, post_id, title, url, status, content):
    """Adds a new post to a local database.

    Parameters:
    ~~~~~~~~~~~
    blog_id : int
        The id of the blog the post belongs to.
    post_id : int
        The id of the post.
    title : str
        The title of the post.
    url : str
        The url of the post.
    status : str
        The status of the post. It can be either 'draft' or 'live'
        (case sensitive).
    content : str
        The HTML markup of the post.
    """
    with get_connection(blog_id) as conn:
        c = conn.cursor()
        post = (post_id, title, url, status, content, time.time())

        c.execute('INSERT INTO posts VALUES (?, ?, ?, ?, ?, ?)', post)


def update_post(blog_id, post_id, title, status, content):
    """Updates a post in a local database.

    Parameters:
    ~~~~~~~~~~~
    blog_id : int
        The id of the blog the post belongs to.
    post_id : int
        The id of the post.
    title : str
        The title of the post.
    status : str
        The status of the post. It can be either 'draft' or 'live',
        case sensitive.
    content : str
        The HTML markup of the post.
    """
    with get_connection(blog_id) as conn:
        c = conn.cursor()
        post = (title, status, content, time.time(), post_id)

        c.execute('UPDATE posts SET title=?, status=?, content=?, updated=?'
                  'WHERE post_id=?', post)


def delete_post(blog_id, post_id):
    """Deletes a post in a local database.

    Parameters:
    ~~~~~~~~~~~
    blog_id : int
        The id of the blog the post belongs to.
    post_id : int
        The id of the post.
    """
    with get_connection(blog_id) as conn:
        c = conn.cursor()

        c.execute('DELETE FROM posts WHERE post_id=?', (post_id,))


def get_post(blog_id, post_id):
    """Retrieves a post from a local database.

    Parameters:
    ~~~~~~~~~~~
    blog_id : int
        The id of the blog the post belongs to.
    post_id : int
        The id of the post.

    Returns:
    ~~~~~~~~
    post : tuple
        A tuple of the post's data. The tuple is in the
        form (post_id, title, url, status, content, last_updated).
    """
    with get_connection(blog_id) as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM posts WHERE post_id = ?', (post_id,))
        post = c.fetchone()

    return post


def get_posts(blog_id, limit=None):
    """Retrieves all the posts from a local database, if a limit
    is specified, it will retrieve up to that amount of posts.

    Parameters:
    ~~~~~~~~~~~
    blog_id : int
        The id of the blog to retrieve posts from.
    limit : int
        The maximum number of posts to retrieve (default None).

    Returns:
    ~~~~~~~~
    posts : list
        A list of tuples containing the retrieved posts' data. The tuple
        is in the form (post_id, title, url, status, content, last_updated).
    """
    with get_connection(blog_id) as conn:
        c = conn.cursor()

        if limit:
            posts = c.execute('SELECT * FROM posts LIMIT ?', (limit,))
        else:
            posts = c.execute('SELECT * FROM posts')

        posts = c.fetchall()

    return posts
