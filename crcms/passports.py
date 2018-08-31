# -*- coding: utf-8 -*-

'''



'''

from .settings import PASSPORT
from http import client
import json


class Passport(object):

    def refresh(self, token: str) -> object:
        pass

    def user(self, token: str):
        response = self._http(PASSPORT['routes']['user'], 'POST', self._request_params({'token': token}))
        if response.status == 200:
            # json.loads(response.read().decode('utf-8')) # or
            return json.loads(response.read(), encoding='utf-8')
        else:
            raise Exception("Request error")

    def check(self, token: str) -> bool:
        # $response = $this->rpc->call(config('foundation.passport.routes.check'), $this->requestParams(
        #     ['token' = > $token]));
        # return $response->getStatusCode() == = 204 | | $response->getStatusCode() == = 200;
        pass

    def logout(self, token: str) -> bool:
        # $response = $this->rpc->method('get')->call(config('foundation.passport.routes.logout'), $this->requestParams(
        # ['token' = > $token]));
        # return $response->getStatusCode() == = 204 | | $response->getStatusCode() == = 200;
        pass

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
        # todo 如果有问题注释测试看下，暂时请求后就关闭连接
        connection.close()
        return connection.getresponse()
