from .context import pyblogit
import pyblogit.api_interface
import pytest
import unittest.mock


def test_get_credentials():
    with unittest.mock.patch('oauth2client.client.flow_from_clientsecrets') as mock_flow, \
            unittest.mock.patch('oauth2client.file.Storage') as MockStorage, \
            unittest.mock.patch('webbrowser.open') as mock_wbopen, \
            unittest.mock.patch('pyblogit.api_interface.input') as mock_input:

        # Set credentials to invalid.
        storage = MockStorage.return_value
        credentials = storage.get.return_value
        credentials.invalid = True

        # Run the method and see if we get what we want.
        result = pyblogit.api_interface.BloggerInterface().get_credentials()

        # Check that the flow was initialised correctly.
        mock_flow.assert_called_with('client_secret.json',
                                     'https://www.googleapis.com/auth/blogger',
                                     redirect_uri='urn:ietf:wg:oauth:2.0:oob')
        MockStorage.assert_called_with('credentials.dat')

        # With invalid credentials, the code should obtain an auth
        # url from the flow and pass it to the browser. Then the
        # authentication code should be taken from input and passed
        # back to the flow for exchange. Test these interactions
        # took place.
        flow = mock_flow.return_value

        flow.step1_get_authorize_url.assert_called_once_with()
        mock_wbopen.assert_called_once_with(
            flow.step1_get_authorize_url.return_value)
        flow.step2_exchange.assert_called_once_with(mock_input.return_value)
        storage.put(flow.step2_exchange.return_value)

        assert result == flow.step2_exchange.return_value


def test_get_service():
    with unittest.mock.patch('pyblogit.api_interface.BloggerInterface.get_credentials') as mock_blogger, \
            unittest.mock.patch('httplib2.Http') as mock_http, \
            unittest.mock.patch('apiclient.discovery.build') as mock_api:

        # Run the method to see if we get what we want.
        result = pyblogit.api_interface.BloggerInterface().get_service()

        # Credentials should be retrieved and used to authorise an
        # http2lib.Http object. This is then used to build an
        # API client. Test these interactions too place.
        credentials = mock_blogger.return_value

        mock_blogger.assert_called_once_with()
        mock_http.assert_called_once_with()
        credentials.authorize.assert_called_once_with(mock_http.return_value)
        mock_api.assert_called_once_with('blogger', 'v3',
                                         http=credentials.authorize.return_value)

        assert result == mock_api.return_value
