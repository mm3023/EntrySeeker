#from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
import os
from.import handlerFunctions





def entry(request):
    #print('---- Main triggered ------ ');
    return HttpResponse("main reporting zeist++");

"""
import datetime;
       



def import_fromjs(request):
    filename="/var/www/html/served_files/"+request.FILES['file'].name+'_'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S");
    print(filename);
        
    new_file=open(filename,'wb');
    new_file.write(request.FILES['file'].read());
    new_file.close();
     
    os.listdir();
    print(os.listdir());
    print(type(os.listdir()));

"""


#@csrf_exempt
def upload(request):
    handlerFunctions.import_fromjs(request);
    return redirect("https://www.verbaloctopus.com/served_files"); 


   
#@csrf_exempt
def input(request):
    context={'message': '--','title':'Verbal Octopus'}
    return render(request,'inputTemplate.html',context);
    #return HttpResponse("success");
    



