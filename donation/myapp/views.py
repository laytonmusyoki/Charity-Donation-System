from django.shortcuts import render, HttpResponse,redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from .decorators import unauthenticated,authenticated
from .forms import UserRegistration
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'index.html')

@authenticated
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if username=='' or password=='':
            messages.warning(request,'All fields are required!')
            return render(request,'accounts/login.html',{"username":username,"password":password})
        else:
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f'We are happy {username} to see you back!')
                return redirect('home')
            else:
                messages.warning(request,'You have entered wrong credentials')
                return render(request,'accounts/login.html',{"username":username,"password":password})
    return render(request,'accounts/login.html')

@authenticated
def register(request):
    form=UserRegistration()
    if request.method=='POST':
        form=UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created successfully for {username}')
            return redirect('signin')
    context={
        "forms":form
    }
    return render(request,'accounts/register.html',context)


def signout(request):
    logout(request)
    messages.warning(request,'You have been logged out')
    return redirect('signin')


def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method=='POST':
        first=request.POST['first']
        last=request.POST['last']
        email=request.POST['email']
        message=request.POST['message']
        subject='New message from '+first+' '+last
        contact=render_to_string('contact_message.html',{'first':first,'last':last,'email':email,'message':message})
        msg=EmailMultiAlternatives(
            subject,
            message,
            email,
            [settings.RECIPIENT_EMAIL],
            reply_to=[email])
        try:
            msg.attach_alternative(contact,'text/html')
            msg.send()
            messages.success(request,f'{first} your message has been sent successfully')
        except Exception as e:
            print(e)
            messages.error(request,'There was an error sending your message')
    return render(request,'contact.html')


def news(request):
    return render(request,'news.html')


def elimu(request):
    return render(request,'elimu.html')


@unauthenticated
def donate(request):
    return render(request,'donate.html')


def health(request):
    return render(request,'better.html')

def family(request):
    return render(request,'family.html')