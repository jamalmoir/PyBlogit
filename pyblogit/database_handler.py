"""
pyblogit.database_handler
~~~~~~~~~~~~~~~~~~~~~~~~~

This module handles the connection and manipulation of the local database.
"""
import sqlite3


def get_connection(blog_id):
    """Connects to a local sqlite database"""
    conn = sqlite3.connect(''.join((str(blog_id), '.db')))

    return conn

def add_blog(blog_id, blog_name):
    """Adds a new blog to the local blogs database and
    creates a new database for the blog."""
    with get_connection('blogs') as conn:
        c = conn.cursor()

        # Check if blogs table exists, if it doesn't create it.
        exists = c.execute('SELECT name FROM sqlite_master WHERE type="table"'
            'AND name="blogs"').fetchone()

        if not exists:
            c.execute('CREATE TABLE blogs(blog_id INT PRIMARY KEY,'
            'blog_name TEXT)')

        c.execute('INSERT INTO blogs VALUES (?, ?)', (blog_id, blog_name))

    with get_connection(blog_id) as conn:
        c = conn.cursor()

        # Create table to store posts in new blog's database.
        c.execute('CREATE TABLE posts(post_id INT PRIMARY KEY, title TEXT,'
                'url TEXT, status TEXT, content TEXT, updated INT)')

def get_blogs():
    """Returns all stored blogs."""
    with get_connection('blogs') as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM blogs')
        blogs = c.fetchall()

    return blogs

def get_post(blog_id, post_id):
    """Retrieves a post from a local database."""
    with get_connection(blog_id) as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM posts WHERE post_id = {p_id}', (post_id,))
        post = c.fetchone()

    return post

def get_posts(blog_id, limit=None):
    """Retrieves all the posts from a local database, if a limit
    is specified, it will retrieve up to that amount of posts."""
    with get_connection(blog_id) as conn:
        c = conn.cursor()

        if limit:
            posts = c.execute('SELECT * FROM posts LIMIT ?', (limit,))
        else:
            posts = c.execute('SELECT * FROM posts')

        posts = c.fetchall()

    return posts

def update_post(blog_id, post_id, post):
    #TODO: update post in local database
    pass

def add_post(blog_id, post):
    #TODO: insert new post in local database
    pass
