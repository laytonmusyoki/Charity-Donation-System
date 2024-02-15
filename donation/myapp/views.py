from django.shortcuts import render, HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index.html')


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
            messages.success(request,'Your message has been sent successfully')
        except Exception as e:
            print(e)
            messages.error(request,'There was an error sending your message')
    return render(request,'contact.html')


def news(request):
    return render(request,'news.html')


def elimu(request):
    return render(request,'elimu.html')


def donate(request):
    return render(request,'donate.html')


def health(request):
    return render(request,'better.html')

def family(request):
    return render(request,'family.html')