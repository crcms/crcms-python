from .passports import Passport
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse
from django.http import HttpResponseRedirect
from .settings import PASSPORT


class AuthMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        # 放行的URL
        if request.path in self._except_path():
            return self.get_response(request)

        # token 验证
        token = self._token(request)
        if token is not None and Passport().check(token) is True:
            return self.get_response(request)
        else:
            return HttpResponseRedirect(reverse('community.login'), {'app_key': PASSPORT['key']})

    def _token(self, request: WSGIRequest) -> str or None:
        if 'token' in request.GET.keys():
            return request.GET['token']
        elif 'Authorization' in request.META.keys():
            return request.META['Authorization']
        else:
            return None

    def _except_path(self) -> tuple:
        return ('/communities/login',)
