"""
pyblogit.database_handler
~~~~~~~~~~~~~~~~~~~~~~~~~

This module handles the connection and manipulation of the local database.
"""
import sqlite3


def get_cursor(blog_id):
    """Connects to a local sqlite database"""
    conn = sqlite3.connect(blog_id)
    c = conn.cursor()

    return c


def add_blog(blog_id, blog_name):
    """Adds a new blog to the local blogs database and
    creates a new database for the blog."""
    # These two statements create the database files if
    # they don't exist.
    c = get_cursor('blogs')
    blog_c = get_cursor(blog_id)

    # Check if blogs table exists, if it doesn't create it.
    exists = bool(c.execute('SELECT name FROM sqlite_master WHERE type="table"
                            AND name="blogs"'))

    if not exists:
        c.execute('CREATE TABLE blogs(blog_id INT, blog_name TEXT)')

    sql = ('INSERT INTO blogs(blog_id, blog_name) values({blog_id},
                                                         {blog_name})'.format(blog_id=blog_id, blog_name=blog_name))

    c.execute(sql)

    # Create table to store posts in new blog's database.
    blog_c.execute('CREATE TABLE posts(post_id INT, title TEXT, url TEXT,
                                       status TEXT, content TEXT, updated INT)')


def get_blogs():
    """Returns all stored blogs."""
    c = get_cursor('blogs')
    blogs = c.execute('SELECT * FROM blogs')

    return blogs


def get_post(blog_id, post_id):
    """Retrieves a post from a local database."""
    c = get_cursor(blog_id)
    sql = 'SELECT * FROM posts WHERE post_id = {p_id}'.format(p_id=post_id)

    c.execute(sql)

    post = c.fetchone()

    return post


def get_posts(blog_id, limit=None):
    """Retrieves all the posts from a local database, if a limit
    is specified, it will retrieve up to that amount of posts."""
    c = get_cursor(blog_id)
    sql = 'SELECT * FROM posts'

    if limit:
        limit = 'LIMIT {lim}'.format(lim=limit)
        sql = ''.join([sql, limit])

    c.execute(sql)

    posts = c.fetchall()

    return posts


def update_post(blog_id, post_id, post):
    # TODO: update post in local database
    pass


def add_post(blog_id, post):
    # TODO: insert new post in local database
    pass
