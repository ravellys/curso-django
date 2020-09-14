from django.http import HttpResponse
# from django.shortcuts import render


# Create your views here.
def home(requests):
    return HttpResponse('<html><body>olá django</body></html>', content_type='text/html')
