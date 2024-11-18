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



#calendar_id="arsaccess2022@gmail.com";
#print("os.path");
#print(os.path);


# If modifying these scopes, delete the file token.json.
#SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]




def holidays():
       
    print("inside holidays-----")
    
    #datetime.today()+timedelta(days=1);
    """
    next_year=datetime.today() + timedelta(days=365);
    next_year=next_year.year
    current_year=datetime.today().year;
    """
    #next_year_str=f'{next_year.year}';
    #print("current_year ",current_year,type(current_year));
    #print("next_year ",next_year,type(next_year));
    #country_holidays('US', years=current_year);
    #country_holidays('US', years=next_year);
    #print("country holidays  ",type(country_holidays('US', years=current_year)) ,country_holidays('US', years=current_year))
    #print("country holidays  subsribe ",type(country_holidays('US', years=current_year)) ,country_holidays('US', years=current_year)[5])
    #count=0;
    #country_holidays('US', years=current_year).items();
    #the_holidays=country_holidays('US', years=current_year);
    #the_holidays.items();
    """
    print("country_holidays('US', years=current_year).items() ---------------------- ",country_holidays('US', years=current_year).items())
    print('the_holidays.items() ---------------------',the_holidays.items())
    print('the_holidays.keys() ---------------------',the_holidays.keys())
    print('list the_holidays.keys()[0]---------------------',list(the_holidays.keys())[0])
    print(' the_holidays.values() ---------------------',the_holidays.values())
    print('list the_holidays.values()[0] ---------------------',list(the_holidays.values())[0])
    print('the_holidays ---------------------',the_holidays)
    """
    
    
    
    holiday_name=[];
    year=[];
    date=[];
    
    next_year=datetime.today() + timedelta(days=365);
    next_year=next_year.year
    current_year=datetime.today().year;
    the_holidays=country_holidays('US', years=current_year);
    the_holidays.items();
    def loop_holiday_api(_year_):
        count=0;
        while count < len(country_holidays('US', years=current_year).keys()):
              holiday_name.append(list(country_holidays('US', years=_year_).values())[count]);
              print('holiday name = ',list(country_holidays('US', years=_year_).values())[count]);
              date.append(list(country_holidays('US', years=_year_).keys())[count]);
              print('date = ',list(country_holidays('US', years=_year_).keys())[count]);
              year.append(current_year);
              count=count+1;
    loop_holiday_api(current_year);
    loop_holiday_api(next_year);
   
   
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





