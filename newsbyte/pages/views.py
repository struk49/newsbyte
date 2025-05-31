from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def terms(request):
    return render(request, 'pages/terms.html')

def privacy(request):
    return render(request, 'pages/privacy.html')

def cookies(request):
    return render(request, 'pages/cookies.html')



def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

