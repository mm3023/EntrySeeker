from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt




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


@csrf_exempt
def upload(request):
    print(request);
    print(request.method);
    print(request.FILES);
    #enctype="multipart/form-data";
    #print(request.FILES.get);
    print(request.FILES.keys());
    return HttpResponse("success");
    

def input():
    context={'message': '--','title':'Verbal Octopus'}
    return render(request,'inputtemplate.html',context);
    



