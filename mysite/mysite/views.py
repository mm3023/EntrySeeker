from django.shortcuts import render
from django.http import HttpResponse


"""    
def my_view(request):
    return render(request, 'my_template.html', {'message': 'Hello from my view!'})



def my_view(request):
    return render(request, {'message': 'Hello from my view!'});
    

def index(request):
    print('---- Index triggered ------ ');
    return HttpResponse("Hello, world. You're at the polls index.");
"""
def entry(request):
    #print('---- Main triggered ------ ');
    return HttpResponse("main reporting zeist++");
def upload(request):
    print(request);
    print(request.method);
    return HttpResponse("success");





