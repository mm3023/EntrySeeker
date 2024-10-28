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
    print(request);
    print(request.method);
    print(request.FILES);
    
    print(os.getcwd());
    os.chdir("/var/www/html/served_files/");
    print(os.listdir());
    print("file name  = ",request.FILES.name);
    os.path.join("/var/www/html/served_files/",request.FILES.name);
    print(os.listdir());

    
    #print(request.query_params);
    #print(request.data);
    #print(request.GET);
    """
    print(request.body);
    print(request.POST);
    print(request.FILES);
    print(request.FILES.keys());
    """
    return HttpResponse("success");



   
#@csrf_exempt
def input(request):
    context={'message': '--','title':'Verbal Octopus'}
    return render(request,'inputTemplate.html',context);
    #return HttpResponse("success");
    



