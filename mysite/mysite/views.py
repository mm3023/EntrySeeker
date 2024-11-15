from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from.import models
from.import handlerFunctions
import os




def entry(request):
    #print('---- Main triggered ------ ');
    return HttpResponse("main reporting zeist++");


#@csrf_exempt
def upload(request):
    handlerFunctions.import_fromjs(request);
    return redirect("input()"); 

def clear_served_files(request):
    handlerFunctions.fileClear();
    return redirect("input()"); 



   
#@csrf_exempt
def input(request):
    context={'message': '--','title':'Verbal Octopus'}
    return render(request,'inputTemplate.html',context);
  

    



