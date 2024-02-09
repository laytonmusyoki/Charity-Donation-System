from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def causes(request):
    return render(request,'causes.html')


def contact(request):
    return render(request,'contact.html')


def news(request):
    return render(request,'news.html')


def volunteer(request):
    return render(request,'volunteer.html')


def donate(request):
    return render(request,'donate.html')