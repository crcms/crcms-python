from .passports import Passport
from django.core.handlers.wsgi import WSGIRequest


class AuthMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        print(type(self.get_response))
        print(request.__class__)
        passport = Passport()

        # passport.check(request.GET['token'] if request.GET['token']
        # not None else )

        # passport.check(request)

        response = self.get_response(request)
        return response

    def _token(self, request: WSGIRequest) -> str:
        if 'token' in request.GET.keys():
            return request.GET['token']
        elif 'Authorization' in request.META.keys():
            return request.META['Authorization']
        else:
            raise Exception('Token not found')
