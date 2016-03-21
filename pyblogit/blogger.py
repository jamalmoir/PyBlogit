"""
pyblogit.blogger
~~~~~~~~~~~~~~~~~~~~~~

This modules acts as an interface between pyblogit and the blogger API.
"""

import oauth2client.client
import oauth2client.file
import apiclient.discovery
import httplib2
import webbrowser
import collections

def get_credentials(self):
    """Gets google api credentials, or generates new credentials
    if they don't exist or are invalid.

    Returns:
    ~~~~~~~~
    credentials : oauth2client.client.OAuth2Credentials
        An OAuth2Credentials object that can be used to
        authorise requests.
    """
    scope = 'https://www.googleapis.com/auth/blogger'

    flow = oauth2client.client.flow_from_clientsecrets(
        'client_secret.json', scope,
        redirect_uri='urn:ietf:wg:oauth:2.0:oob')

    storage = oauth2client.file.Storage('credentials.dat')
    credentials = storage.get()

    if not credentials or credentials.invalid:
        auth_uri = flow.step1_get_authorize_url()
        webbrowser.open(auth_uri)

        auth_code = input('Enter the auth code: ')
        credentials = flow.step2_exchange(auth_code)

        storage.put(credentials)

    return credentials

def get_service(self):
    """Returns an authorised blogger api service.

    Returns:
    ~~~~~~~~
    service : apiclient.discovery.Resource
        A Resource object with methods for interacting with the
        blogger service.
    """
    credentials = self.get_credentials()
    http = httplib2.Http()
    http = credentials.authorize(http)
    service = apiclient.discovery.build('blogger', 'v3', http=http)

    return service

def get_blog(self, blog_id):
    """Gets the details ofthe blog withthe id blog_id.

    Parameters:
    ~~~~~~~~~~~
    blog_id : int
        The id of the blog to get.

    Returns:
    ~~~~~~~~
    blog : namedtuple
        A named tuple containing the blog's details. The namedtuple
        is in the form (blog_id, name, desc, url).
    """
    BlogDetails = collections.namedtuple(
        'BlogDetails', 'blog_id, name, desc, url')

    conn = self.get_service()
    request = conn.blogs().get(blogId=blog_id, view='ADMIN')
    response = request.execute()

    name = response.get('name')
    desc = response.get('description')
    url = response.get('url')

    blog = BlogDetails(blog_id=blog_id, name=name, desc=desc, url=url)

    return blog

def get_posts(self, blog_id, status='live'):
    """Gets all posts from the blog with the id blog_id.

    Parameters:
    ~~~~~~~~~~~
    blog_id : int
        The id of the blog to get posts from.
    status : string
        The status of which type of post to get. It can be either
        'live' or 'draft' (case sensitive, default 'live')

    Returns:
    ~~~~~~~~
    posts : list
        A list of dictionaries containing a blogs posts. The dictionaries
        are in the form {post_id, title, url, status, content}.
    """
    posts = []

    conn = self.get_service()
    request = conn.posts().list(blogId=blog_id, view='ADMIN',
                                status=status)

    # Responses are paginated, so a paging loop is required.
    while request:

        response = request.execute()

        for post in response.get('items', []):
            post_id = post.get('id')
            title = post.get('title')
            url = post.get('url')
            status = post.get('status')
            content = post.get('content')

            posts.append({'post_id': post_id, 'title': title, 'url': url,
                          'status': status, 'content': content})

        request = conn.posts().list_next(request, response)

    return posts

def add_post(self, blog_id, post, is_draft=True):
    """Adds a new post to the blog with the id blog_id.

    Parameters:
    ~~~~~~~~~~~
    blog_id : int
        The id of the blog to add a post to.
    post : tuple
        A tuple containing the new posts details. The tuple is in the
        form (title, content, (labels), author_name, author_id).
    is_draft : bool
        A boolean indicating whether the post is a draft
        or not (default True).

    Returns:
    ~~~~~~~~
    post_id : int
        The id of the newly created post.
    """
    conn = self.get_service()

    title, content, author_name, author_id, labels = post

    data = {
        'kind': 'blogger#post',
        'title': title,
        'content': content,
        'labels': labels,
        'author': {'displayName': author_name, 'id': author_id}
    }

    request = conn.posts().insert(blogId=blog_id, body=data,
                                  isDraft=is_draft)
    response = request.execute()
    post_id = response.get('id')

    return post_id

def edit_post(self, blog_id, post_id, post):
    """Edits an existing post with the id post_id from the blog
    with the id blog_id.

    Parameters:
    ~~~~~~~~~~~
    blog_id : int
        The id of the blog to edit a post of.
    post_id : int
        The id of the post to edit.
    post : tuple
        A tuple containing the new posts details. The tuple is in the
        form (title, content, (labels), author_name, author_id).

    Returns:
    ~~~~~~~~
    updated : timestamp
        A timestamp of the time the post was updated.
    """
    conn = self.get_service()

    title, content, labels = post

    data = {
        'title': title,
        'content': content,
        'labels': labels
    }

    request = conn.posts().update(blogId=blog_id, postId=post_id, body=data)
    response = request.execute()
    updated = response.get('updated')

    return updated

def delete_post(self, blog_id, post_id):
    """Deletes an existing post with the id post_id from the blog
    with the id blog_id.

    Parameters:
    ~~~~~~~~~~~
    blog_id : int
        The id of the blog to delete a post from.
    post_id : int
        The id of the post to delete.
    """
    conn = self.get_service()

    request = conn.posts().delete(blogId=blog_id, postId=post_id)
    request.execute()
