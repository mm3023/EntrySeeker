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

def entry(request):
    #print('---- Main triggered ------ ');
    return HttpResponse("You're at the main-entry.");
"""
    
"""
def index(request):
    print('---- Index triggered ------ ');
    return HttpResponse("Hello, world. You're at the TS1 index.");
"""
def index(request):
    title='VerbalOctopus';
    return render(request,'template.html',title,{'message': 'Hello from my TS1Proj!'});
