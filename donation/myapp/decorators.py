from django.shortcuts import redirect
from django.contrib import messages

def unauthenticated(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            messages.info(request, 'You need to login first before you make your donation')
            return redirect('signin')
    return wrapper


def authenticated(view_func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'You need to logout first')
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
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