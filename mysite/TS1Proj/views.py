from django.shortcuts import render
from django.http import HttpResponse

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
print(response.json());






def index(request):
        context={'message': 'Hello from my TS1Proj!','title':'Verbal Octopus'}
        return render(request,'template.html',context);
