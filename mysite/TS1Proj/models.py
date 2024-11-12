import requests;
import json
import pandas
from datetime import datetime
from django import forms

#google api imports
from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials   
from datetime import datetime, timedelta   




"""
from django.db import models

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
#zeist_initiate();
"""
def JsonRequestResolver1(x):
        #test_for_string=type(x);
        if type(x)!=type('x'):
            print('string expected')
            return'string expected';
        else:
            #x is the URL appropriately structured;
            response=requests.get(x).json();
            resFrame=pandas.DataFrame(response);
            #reFrame=[item.split(",") for item in resFrame];
        return resFrame;





def open_holiday_DataFrame():
    dateString=str(datetime.now())[0:10];
    #original URL from documentation openholidaysapi 'https://openholidaysapi.org/PublicHolidaysByDate?languageIsoCode=DE&date=2023-12-25';
    #print('https://openholidaysapi.org/PublicHolidaysByDate?languageIsoCode=DE&date=2023-12-25')
    URL='https://openholidaysapi.org/PublicHolidaysByDate?languageIsoCode=DE&date='+dateString;
    print('URL');
    print(URL);
    return JsonRequestResolver1('https://openholidaysapi.org/PublicHolidaysByDate?languageIsoCode=DE&date=2023-12-25');



def nagerAPI():
     
     dateString=str(datetime.now())[0:4];
     
     
     print(dateString);
     print(type(dateString));
     
     #Original URL from docs 'https://date.nager.at/api/v3/PublicHolidays/2024/US'
     URL='https://date.nager.at/api/v3/PublicHolidays/'+dateString+'/US'
     print('URL');
     print(URL);
     return JsonRequestResolver1(URL);
     
    
#open_holiday_DataFrame();
     

#open_holiday_set=JsonRequestResolver1('https://openholidaysapi.org/PublicHolidaysByDate?languageIsoCode=DE&date=2023-12-25');




#print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::");
#print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::");

#nager api alter year/country code;
#https://date.nager.at/api/v3/PublicHolidays/2024/US
#print('open_holiday_DataFrame()');
#print(open_holiday_DataFrame());

#date_nager_at=JsonRequestResolver1('https://date.nager.at/api/v3/PublicHolidays/2024/US');
#print('nagerAPI()');
#print(nagerAPI());



