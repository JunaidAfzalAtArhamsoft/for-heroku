from ManageTask.models import Person
from django.http import HttpResponseForbidden, HttpResponseRedirect


class RestrictUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_user = request.user
        print(current_user)
        person = Person.objects.filter(username=current_user)
        allow_routes = ['/ManageTask/', '/ManageTask/login/', '/ManageTask/logout', '/ManageTask/register/']
        if len(person) != 0:
            response = self.get_response(request)
            return response
        elif request.path in allow_routes:
            response = self.get_response(request)
            return response
        else:
            return HttpResponseForbidden('<h1>You are not allowed to View This Page</h1>')

    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     current_user = request.user
    #     person = Person.objects.filter(username=current_user)
    #     allow_roues = ['/ManageTask/', '/ManageTask/login/', '/ManageTask/logout', '/ManageTask/register/']
    #     if len(person) != 0:
    #         response = self.get_response(request)
    #         return response
    #     else:
    #         if request.path in allow_roues:
    #             return None
    #         return HttpResponseForbidden('<h1>You are not allowed to View This Page</h1>')
    #

