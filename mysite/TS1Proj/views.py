from django.shortcuts import render
from django.http import HttpResponse

def zeist_initiate():
    print("zeist is online");
    return 0;
zeist_initiate()

def index(request):
        context={'message': 'Hello from my TS1Proj!','title':'Verbal Octopus'}
        return render(request,'template.html',context);
