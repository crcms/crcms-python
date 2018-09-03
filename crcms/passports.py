# -*- coding: utf-8 -*-

'''



'''

from .settings import PASSPORT
from http import client
import json


class Passport(object):

    def refresh(self, token: str) -> dict:
        try:
            response = self._http(PASSPORT['routes']['refresh'], 'POST', self._request_params({'token': token}))
            if response.status == 200:
                # json.loads(response.read().decode('utf-8')) # or
                return json.loads(response.read(), encoding='utf-8')
            else:
                raise Exception("Request error")
        except(Exception):
            raise Exception("Net error")

    def user(self, token: str) -> dict:
        try:
            response = self._http(PASSPORT['routes']['user'], 'POST', self._request_params({'token': token}))
            if response.status == 200:
                # json.loads(response.read().decode('utf-8')) # or
                return json.loads(response.read(), encoding='utf-8')
            else:
                raise Exception("Request error")
        except(Exception):
            raise Exception("Net error")

    def check(self, token: str) -> bool:
        try:
            response = self._http(PASSPORT['routes']['check'], 'POST', self._request_params({'token': token}))
            return response.status == 204 or response.status == 200
        except(Exception):
            raise Exception("Net error")

    def logout(self, token: str) -> bool:
        try:
            response = self._http(PASSPORT['routes']['logout'], 'GET', self._request_params({'token': token}))
            return response.status == 204 or response.status == 200
        except(Exception):
            raise Exception("Net error")

    def _request_params(self, params: dict) -> dict:
        # return params.update({'app_key': PASSPORT.get('key'), 'app_secret': PASSPORT.get('secret')})
        params.update({'app_key': PASSPORT.get('key'), 'app_secret': PASSPORT.get('secret')})
        return params

    def _http(self, url: str, method: str = 'GET', params: dict = None) -> client.HTTPResponse:
        connection = client.HTTPConnection(PASSPORT['host'], timeout=10)
        connection.request(method, url, None if params is None else json.dumps(params), {
            'Accept': 'application/json',
            'Content-type': 'application/json',
        })
        return connection.getresponse()
