from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
import os
from.import handlerFunctions
import threading

#xfs="cat";
def kprint(xfs):
    print(xfs);
    return 0;
print("Load inficator");
kprint("cracker-barrel");
threading.Thread(target=kprint('dog'));




def entry(request):
    #print('---- Main triggered ------ ');
    return HttpResponse("main reporting zeist++");


#@csrf_exempt
def upload(request):
    handlerFunctions.import_fromjs(request);
    
    #import_frojs=threading.Thread(target=handlerFunctions.import_fromjs, args=(request));
    #import_frojs.start();

    
    return redirect("input()"); 

def clear_served_files(request):
    handlerFunctions.fileClear();
    """
    print("os.getcwd()--",os.getcwd());
    os.chdir("/var/www/html/served_files")
    print("os.getcwd()--",os.getcwd());
    print("os.listdir() -- ",os.listdir());
    for files in os.listdir() :
        os.remove(files);
    print("os.listdir() -- ",os.listdir());    
        
    #return redirect('clear_served_files()');
    """
    return 0;
    


   
#@csrf_exempt
def input(request):
    context={'message': '--','title':'Verbal Octopus'}
    return render(request,'inputTemplate.html',context);
    #return HttpResponse("success");

    



