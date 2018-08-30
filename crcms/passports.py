# -*- coding: utf-8 -*-

'''



'''

from .settings import PASSPORT
from http import client
from urllib import parse
import json


class Passport(object):

    def refresh(self, token: str) -> object:
        pass

    def user(self, token: str):
        # params = parse.urlencode(self._requestParams({'token':token}))

        print(self._requestParams({'token':token}))
        data = json.dumps(self._requestParams({'token':token}))
        print(data)

        connection = client.HTTPConnection(PASSPORT['host'],timeout=10)
        connection.request('POST',PASSPORT['routes']['user'],data,{
            'Accept':'application/json',
            'Content-type':'application/json',
        })
        response = connection.getresponse()
        # print(response.status,response.reason,response.read())
        json.loads(response.read(), 'utf-8')
        print(json.loads(response.read(),'utf-8'))#json.JSONDecoder.decode(response.read().decode('utf-8'))
        # {
        # return $this->rpc->call(config('foundation.passport.routes.user'), $this->requestParams(['token' = > $token]));
        # }
        # pass

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

    def _requestParams(self, params: dict) -> dict:
        # return params.update({'app_key': PASSPORT.get('key'), 'app_secret': PASSPORT.get('secret')})
        params.update({'app_key': PASSPORT.get('key'),'app_secret': PASSPORT.get('secret')})
        return params

    def _get_response(self):
        pass