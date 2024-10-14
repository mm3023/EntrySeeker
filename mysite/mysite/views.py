from django.shortcuts import render
from django.http import HttpResponse
"""
def my_view(request):
    return render(request, 'my_template.html', {'message': 'Hello from my view!'})
"""    
def my_view(request):
    return render(request, 'my_template.html', {'message': 'Hello from my view!'})






def index(request):
    return HttpResponse("Hello, world. You're at the not-polls index.")
