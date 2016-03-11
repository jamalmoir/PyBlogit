"""
pyblogit.api_interface
~~~~~~~~~~~~~~~~~~~~~~

This modules acts as an interface between pyblogit and various
blogging platform apis.
"""

import oauth2client.client
import oauth2client.file
import apiclient.discovery
import httplib2
import json
import webbrowser
import collections

class BloggerInterface(object):
    """Connects to blogger api and authorises client."""

    def get_credentials(self):
        """Gets google api credentials, or generates new credentials
        if they don't exist or are invalid."""
        client_id = ''
        client_secret = ''
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
        """Returns an authorised blogger api service."""
        credentials = self.get_credentials()
        http = httplib2.Http()
        http = credentials.authorize(http)
        service = apiclient.discovery.build('blogger', 'v3', http=http)

        return service

    def get_blog(self, blog_id):
        """Grabs blog details"""
        BlogDetails = collections.namedtuple('BlogDetails', 'blog_id, name, desc, url')

        conn = self.get_service()
        request = conn.blogs().get(blogId=blog_id, view='AUTHOR')
        response = request.execute()

        name = response.get('name')
        desc = response.get('description')
        url = response.get('url')

        blog = BlogDetails(blog_id=blog_id, name=name, desc=desc, url=url)

        return blog
