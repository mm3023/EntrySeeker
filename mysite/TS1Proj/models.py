from __future__ import print_function;

from google.auth.transport.requests import Request;
from google.oauth2.credentials import Credentials;
from googleapiclient.discovery import build;
from googleapiclient.errors import HttpError;
from google_auth_oauthlib.flow import InstalledAppFlow;
from holidays import country_holidays

from datetime import datetime,date,timedelta; 
import os.path;
import requests;
import json;
import pandas;
from django import forms;
import holidays;

_10_days_from_now=datetime.today() + timedelta(days=10);
holiday_doc=pandas.read_csv('TS1Proj/geminiholidays.csv');


#print(holiday_doc);











#calendar_id="arsaccess2022@gmail.com";
#If modifying these scopes, delete the file token.json.
#SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]




def holidays():
       
    print("inside holidays-----");
    print(datetime.now().month)
    print(datetime.now().day)   
    _10_days_from_now=datetime.today() + timedelta(days=10);
    print(_10_days_from_now)   
    #print(datetime.now().day - timedelta(days=10))   
    holiday_doc=pandas.read_csv('TS1Proj/geminiholidays.csv');   
    print(holiday_doc);   
  


    
    
    
    holiday_name=[];
    #year=[];
    date=[];
    data={'holiday_name':holiday_name,'date':date}
    next_year=datetime.today() + timedelta(days=365);
    next_year=next_year.year
    current_year=datetime.today().year;
    the_holidays=country_holidays('US', years=current_year);
    
    the_holidays.items();
   
    def loop_holiday_api(_year_):
        count=0;
        while count < len(country_holidays('US', years=_year_).keys()):
              holiday_name.append(list(country_holidays('US', years=_year_).values())[count]);
              #print('holiday name = ',list(country_holidays('US', years=_year_).values())[count]);
              date.append(list(country_holidays('US', years=_year_).keys())[count]);
              print('key type',type(list(country_holidays('US', years=_year_).keys())[count]))
               
              #print('date = ',list(country_holidays('US', years=_year_).keys())[count]);
              #year.append(_year_);
              count=count+1;
    #loop_holiday_api(current_year);
    loop_holiday_api(next_year);
   
    #synthetic_cal=pandas.DataFrame([holiday_name,year,date]);  
    synthetic_cal2=pandas.DataFrame(data);      
    #synthetic_cal_2manybrackets=pandas.DataFrame([holiday_name,year,date]);      

       
  
       
  
    #holiday_doc1=pandas.read_csv('holiday.csv').drop(['category','begin','end','rule'], axis=1);  
    #holiday_doc2=pandas.read_csv('new_holidays.csv'); 
    
    #holiday_doc3=pandas.read_csv('TS1Proj/geminiholidays.csv');      

       
    #rint(synthetic_cal);  
    print(synthetic_cal2);   
    #print(synthetic_cal_2manybrackets);   
    #print(holiday_doc3);    
    print('end holidays')
   
    return 0;
holidays();    



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

#generic calender holidays
def open_holiday_DataFrame():
    dateString=str(datetime.now())[0:10];
    #original URL from documentation openholidaysapi 'https://openholidaysapi.org/PublicHolidaysByDate?languageIsoCode=DE&date=2023-12-25';
    #print('https://openholidaysapi.org/PublicHolidaysByDate?languageIsoCode=DE&date=2023-12-25')
    URL='https://openholidaysapi.org/PublicHolidaysByDate?languageIsoCode=DE&date='+dateString;
    print('URL');
    print(URL);
    return JsonRequestResolver1('https://openholidaysapi.org/PublicHolidaysByDate?languageIsoCode=DE&date=2023-12-25');


"""

#deprecate? troubleshoot? usually empty
def nagerAPI():
    dateString=str(datetime.now())[0:4];
    print(dateString);
    print(type(dateString));
     
    #Original URL from docs 'https://date.nager.at/api/v3/PublicHolidays/2024/US'
    URL='https://date.nager.at/api/v3/PublicHolidays/'+dateString+'/US'
    print('URL');
    print(URL);
    return JsonRequestResolver1(URL);
"""     
    






#nager api alter year/country code; deprecated?
#https://date.nager.at/api/v3/PublicHolidays/2024/US

#print('open_holiday_DataFrame() active ');
#print(open_holiday_DataFrame());





