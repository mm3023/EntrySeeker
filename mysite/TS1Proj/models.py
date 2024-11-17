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
    
    next_year=datetime.today() + timedelta(days=365);
    current_year=datetime.today().year;
    next_year_str=f'{next_year.year}';
    print("current_year ",current_year,type(current_year));
    print("next_year ",next_year,type(next_year));
    country_holidays('US', years=current_year);
    print("country holidays ",country_holidays('US', years=current_year))

    
    #today_str=f'{date.today()}';
    #end_date_str=f'{end_date}';
    #print(end_date);
    #print("year - ",datetime.today().year)
    #print('Today ',today_str);
    #print('end day ',end_date_str);

    #print(country_holidays('US', years=)[today_str:end_date_str]);
    #print();
    
    #print(country_holidays('US').get('2026-01-01'));
    #print(type(country_holidays('US')['2024-01-01':'2025-01-03']));
    print("string manual inputs - ",country_holidays('US')['2014-01-01':'2014-01-03']);
    #print(country_holidays('US', years=2024));
    print("manual year ",country_holidays('US', years=2025));
    country_holidays('US')['2014-01-01':'2014-01-03'];
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





