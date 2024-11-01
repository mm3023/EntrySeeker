#from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
import os

"""

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['file']

def upload_file(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
           # return redirect('success_page')  
            # return ;
  # Redirect to a success page
    else:
        form = MyForm()
    return render(request, 'upload_form.html', {'form': form})
"""



"""    


def my_view(request):
    return render(request, {'message': 'Hello from my view!'});
    


"""
def entry(request):
    #print('---- Main triggered ------ ');
    return HttpResponse("main reporting zeist++");

import datetime;
#@csrf_exempt
def upload(request):
    print(type(datetime.datetime.now()));
    print(datetime.datetime.now())
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("------------------------------------------")
    filename="/var/www/html/served_files/"+request.FILES['file'].name+'_'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S");
    print(filename);
    """
    print(os.getcwd());
    os.chdir("/var/www/html/served_files/");
    print(os.getcwd());
    print(os.listdir());
    #print("file name  = ",filename);
    path=request.FILES['file'].name
    print(os.listdir());
    print(path);
    """
    print("-------------------------------------------------------------------");
    new_file=open(filename,'wb');
    new_file.write(request.FILES['file'].read());
    new_file.close();
     
    os.listdir();
    print(os.listdir());
    print(type(os.listdir()));
    
 
    #return HttpResponse("success");
    return redirect("https://www.verbaloctopus.com/served_files"); 


   
#@csrf_exempt
def input(request):
    context={'message': '--','title':'Verbal Octopus'}
    return render(request,'inputTemplate.html',context);
    #return HttpResponse("success");
    



