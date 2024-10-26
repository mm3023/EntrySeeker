#from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from * import models

"""
def upload_file(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')   
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
    #print(request.query_params);
    #print(request.data);
    print(request.GET);
    print(request.body);
    print(request.POST);
    print(request.method);
    print(request.FILES);
    print(request.FILES.keys());
    return HttpResponse("success");



   
@csrf_exempt
def input(request):
    context={'message': '--','title':'Verbal Octopus'}
    return render(request,'inputTemplate.html',context);
    #return HttpResponse("success");
    



