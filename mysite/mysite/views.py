#from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
import os
#import models

"""
from django.db import models

class MyModel(models.Model):
    file = models.FileField(upload_to='uploads/')
    




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
    import datetime;
    
    filename=request.FILES['file'].name+datetime.now();
    def replicate_file_check(a,b):
        if b in a:
           return "duplicate";
        else:
           return "first";
    
    """
    print(request.FILES.keys);
    print(request.FILES.items());
    print(request.FILES['file']);
    """   
    print(os.getcwd());
    os.chdir("/var/www/html/served_files/");
    print(os.getcwd());
    print(os.listdir());
    print("file name  = ",filename);
    path=request.FILES['file'].name
    print(os.listdir());
    print(path);
    print("-------------------------------------------------------------------");
    new_file=open(path,'wb');
    new_file.write(request.FILES['file'].read());
    new_file.close();

    """
    print(replicate_file_check(os.listdir(),filename));
    
    if replicate_file_check(os.listdir(),filename)="first":
        new_file=open(path,'wb');
        new_file.write(request.FILES['file'].read());
        new_file.close();
    """
    os.listdir();
    print(os.listdir());
    print(type(os.listdir()));
    
  
     
    
  
    return HttpResponse("success");



   
#@csrf_exempt
def input(request):
    context={'message': '--','title':'Verbal Octopus'}
    return render(request,'inputTemplate.html',context);
    #return HttpResponse("success");
    



