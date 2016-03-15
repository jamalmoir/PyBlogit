from .context import pyblogit
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
            #credentials.invalid = True
            credentials = None

            #run the method and see if we get what we want.
            result = pyblogit.api_interface.BloggerInterface().get_credentials()

            #check that the flow was initialised correctly.
            mock_flow.assert_called_with('client_secret.json',
                'https://www.googleapis.com/auth/blogger',
                redirect_uri='urn:ietf:wg:oauth:2.0:oob')
            MockStorage.assert_called_with('credentials.dat')

            # With invalid credentials, the code should obtain an auth
            # url from the flow and pass it to the browser. Then the
            # authentication code should be taken from input and passed
            # back to the flow for exchange. Test these interactions
            # took place.
            mock_flow.step1_get_authorize_url.assert_called_once_with()
            mock_wbopen.assert_called_once_with(mock_flow.step1_get_authorize_url.return_value)
            mock_flow.step2_exchange.assert_called_once_with(mock_input.return_value)
            storage.put(mock_flow.step2_exchange.return_value)
            assert result == mock_flow.step2_exchange.return_value
