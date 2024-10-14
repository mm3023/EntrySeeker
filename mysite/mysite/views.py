from django.shortcuts import render
from django.http import HttpResponse

def signal2():
    print("signal 2 that views is running");
"""
def my_view(request):
    return render(request, 'my_template.html', {'message': 'Hello from my view!'})
"""    
def index():
    print('---- Index triggered ------ ');
    return HttpResponse("Hello, world. You're at the polls index.");






