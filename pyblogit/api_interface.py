"""
pyblogit.api_interface
~~~~~~~~~~~~~~~~~~~~~~

This modules acts as an interface between pyblogit and various
blogging platform apis.
"""

import oauth2client.client
import oauth2client.file
import httplib2

class BloggerInterface(object):
    """Connects to blogger api and authorises client."""

    def __init__(self):
        #TODO

    def get_credentials(self):
        """Gets google api credentials, or generates new credentials
        if they don't exist or are invalid."""
        client_id = ''
        client_secret = ''
        scope = 'https://www.googleapis.com/blogger'

        flow = oasuth2client.client.OAuth2WebServerFlow(client_id,
                client_secret, scope)
        storage = oauth2client.file.Storage('credentials.dat')
        credentials = storage.get()

        if not credentials or credientials.invalid:
            credentials = tools.run_flow(flow, storage,
                    tools.argparser.parse_args())

        return credentials

    def get_service(self):
        """Returns an authorised blogger api service."""
        credentials = self.get_credentials()
        http = httplib2.Http()
        http = credentials.authorize(http)
        service = build('blogger', 'v3', http=http)

        return service
