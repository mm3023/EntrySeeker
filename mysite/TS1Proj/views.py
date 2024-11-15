from django.shortcuts import render
from django.http import HttpResponse
from TS1Proj import models

#from django.db import models
"""
class MyModel(models.Model):
    file = models.FileField(upload_to='uploads/')
class MyModel(models.Model):
    file = models.FileField(upload_to='uploads/')



class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['file']
"""
"""
def zeist_initiate():
    print("zeist is online");
    return 0;
zeist_initiate();
import requests;
#response = requests.get('https://api.github.com/user', auth=('user', 'pass'))
#https://openholidaysapi.org/PublicHolidaysByDate?languageIsoCode=DE&date=2023-12-25
response = requests.get('https://openholidaysapi.org/PublicHolidaysByDate?languageIsoCode=DE&date=2023-12-25');
print('request sent');
print('response');
print(response);
print(response.json()[1]);



#nager api alter year/country code;
#https://date.nager.at/api/v3/PublicHolidays/2024/US
response = requests.get('https://date.nager.at/api/v3/PublicHolidays/2024/US');
print(response.json()[1]);


"""



def index(request):
        context={'message': 'Hello from my TS1Proj!','title':'Verbal Octopus'}
        return render(request,'template.html',context);
