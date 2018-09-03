from .passports import Passport
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse
from django.http import HttpResponseRedirect
from .settings import PASSPORT
from community.models import User


class AuthMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        # 放行的URL
        if self._except_path(request) is False:
            return self.get_response(request)

        # token 验证
        token = self._token(request)

        passport = Passport()
        if token is not None and passport.check(token) is True:
            # 绑定 user
            request.user = User(**passport.user(token)['data'])
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

    def _except_path(self, request: WSGIRequest) -> bool:
        list = ('/communities/login', '/admin*')
        for path in list:
            if request.path == path or request.path.find(path) > -1:
                return True
        return False
