#from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
import os
from.import handlerFunctions
#import handlerFunctions





def entry(request):
    #print('---- Main triggered ------ ');
    return HttpResponse("main reporting zeist++");


#@csrf_exempt
def upload(request):
    handlerFunctions.import_fromjs(request);
    return redirect("upload()"); 

def clear_served_files(request):
    print("os.getcwd()--",os.getcwd());
    os.chdir("/var/www/html/served_files")
    print("os.getcwd()--",os.getcwd());
    print("os.listdir() -- ",os.listdir());
    for files in os.listdir() :
        os.remove(files);
    print("os.listdir() -- ",os.listdir());    
        
    #return redirect('clear_served_files()');
    return 0;
    


   
#@csrf_exempt
def input(request):
    context={'message': '--','title':'Verbal Octopus'}
    return render(request,'inputTemplate.html',context);
    #return HttpResponse("success");

    



