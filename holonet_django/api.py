# -*- coding: utf8 -*-
import json

from oauthlib.oauth2 import BackendApplicationClient, TokenExpiredError
from requests.exceptions import RequestException
from requests_oauthlib import OAuth2Session

from .constants import API_OAUTH_TOKEN
from .exceptions import HolonetAuthenticationFailiure, HolonetRequestFailiure
from .settings import holonet_settings
from .utils import create_url


class APIClient(object):

    oauth_client = BackendApplicationClient(client_id=holonet_settings.API_CLIENT_ID)
    holonet_client = None

    def _fetch_client(self):
        if self.holonet_client is None:
            self.holonet_client = OAuth2Session(client=self.oauth_client)
            self._refresh_token()

        return self.holonet_client

    def _refresh_token(self):
        if self.holonet_client is None:
            self._fetch_client()

        try:
            self.holonet_client.fetch_token(token_url=create_url(API_OAUTH_TOKEN, api_path=False),
                                            client_id=holonet_settings.API_CLIENT_ID,
                                            client_secret=holonet_settings.API_CLIENT_SECRET)
        except RequestException as ex:
            print(ex)
            raise HolonetAuthenticationFailiure('Could not retrieve access token. Please '
                                                'check the API_CLIENT_ID and API_CLIENT_SECRET '
                                                'settings.')

    def _do_request(self, name, url, **kwargs):
        def request():
            f = getattr(self._fetch_client(), name)
            response = f(create_url(url), **kwargs)
            if 200 <= response.status_code < 300:
                return json.loads(response.text)
            else:
                raise HolonetRequestFailiure(response)

        try:
            return request()
        except TokenExpiredError:
            self._refresh_token()
            return request()

    def get(self, url, **kwargs):
        return self._do_request('get', url, **kwargs)

    def post(self, url, data, **kwargs):
        kwargs['data'] = data
        return self._do_request('post', url, **kwargs)

client = APIClient()
