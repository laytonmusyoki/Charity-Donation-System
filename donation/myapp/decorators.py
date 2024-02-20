from django.shortcuts import redirect
from django.contrib import messages

def unauthenticated(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            messages.warning(request, 'You need to login first')
            return redirect('login')
    return wrapper


def allowed_users(user_roles=[]):
    def decorators(view_func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in user_roles:
                return view_func(request, *args, **kwargs)
            else:
                messages.warning(request, 'You are not authorized to view this page')
                return redirect('home')
        return wrapper
    return decorators