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
    return redirect("https://www.verbaloctopus.com/served_files"); 

def clear_served_files(request):
    print("os.getcwd()--",os.getcwd());
    os.chdir("/var/www/html/served_files")
    print("os.getcwd()--",os.getcwd());
    print("os.listdir() -- ",os.listdir());
    for files in os.listdir() :
        os.remove(files);
    print("os.listdir() -- ",os.listdir());    
    #print("----permissions R ?--",os.access(os.getcwd(),os.R_OK));
    #print("find True ",str(os.access(os.getcwd(),os.R_OK)).find("True"));
    """
    File_Path-=os.getcwd();
    if str(os.access(File_Path-,os.W_OK)).find("True"):
       print("Permission to Write");
    else: 
        print("Permission not given chmod");
    if     
    print("check 1");
    """
    
    
    
    
    """
    print("os.getcwd()--",os.getcwd());
    os.chdir("/var/www/html/served_files")
    print("os.getcwd()--",os.getcwd());
    print("os.listdir() -- ",os.listdir());
    





    
    print("----permissions R ?--",os.access(os.getcwd(),os.R_OK));
    print("os.listdir()[0]----",os.listdir()[0]);
    print("os.listdir()[1]----",os.listdir()[1]);
    print("os.listdir()[2]----",os.listdir()[2]);
    print("check point 1")
    os.path.isfile(os.listdir()[0]).find('True');
    os.path.isfile(os.listdir()[0])
    print("check point 2")
    print(os.path.isfile(os.listdir()[0]));
    print(type(os.path.isfile(os.listdir()[0])));
    print("check point 3")
    print(os.path.isfile(os.listdir()[0]));
    print("check point 4")
    os.listdir()[0].find('/')
    print("check point 5")
    str(os.path.isfile(os.listdir()[0]))
    print(str(os.path.isfile(os.listdir()[0])))
    print(type(str(os.path.isfile(os.listdir()[0]))))
    print("check point 6")
    str(os.path.isfile(os.listdir()[0])).find('/');
    print(str(os.path.isfile(os.listdir()[0])).find('/'))
    
    print(os.path.isfile(os.listdir()[0]).find('/'));
    print("check point 7")
    """
    return 0;
    


   
#@csrf_exempt
def input(request):
    context={'message': '--','title':'Verbal Octopus'}
    return render(request,'inputTemplate.html',context);
    #return HttpResponse("success");

    



