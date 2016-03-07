"""
pyblogit.api_interface
~~~~~~~~~~~~~~~~~~~~~~

This modules acts as an interface between pyblogit and various
blogging platform apis.
"""

import gdata.gauth
import gdata.blogger.client

class BloggerInterface(object):

    def __init__(self):
        self._CLIENT_ID = client_id
        self._CLIENT_SECRET = client_secret
        self._SCOPE = 'https://www.googleapis.com/auth/blogger'

    def get_access_code(self):
        """Opens dafualt browser to the google auth page and provides
        them with an access code."""
        token = gdata.gauth.OAuth2Token(
                client_id = self.CLIENT_ID,
                client_secret = self.CLIENT_SECRET,
                scope = self.SCOPE,
                user_agent = 'pyblogit')

        url = token.generate_authorize_url(redirect_uri='urn:ietf:wg:oauth:2.0:oob')

        webbrowser.open_new_tab(url)

    def generate_token(self, code):
        """Generates new api access token."""
            self._token = token.get_access_token(code)

    def get_client(self):
        """Returns an authorised blogger api client."""
        client = gdata.blogger.client.BloggerClient()
        self._token.authorize(client)

        return client
