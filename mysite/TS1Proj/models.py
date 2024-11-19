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
    current_month=datetime.now().month;
    current_day=datetime.now().day;   
       
    print("inside holidays-----");
    #print(datetime.now().month)
    #print(datetime.now().day)   
    _10_days_from_now=datetime.today() + timedelta(days=10);
    holiday_doc=pandas.read_csv('TS1Proj/geminiholidays.csv');  
        
    holiday_name=[];
    Month=[];
    Day=[];
    date=[];
    reconstructed_date=[];
    data={'Holiday Name':holiday_name,'Month':Month,'Day':Day}
    next_year=datetime.today() + timedelta(days=365);
    next_year=next_year.year
    current_year=datetime.today().year;
    the_holidays=country_holidays('US', years=current_year);
    
  
    def loop_holiday_api(_year_):
        count=0;
        while count < len(country_holidays('US', years=_year_).keys()):
              holiday_name.append(list(country_holidays('US', years=_year_).values())[count]);
              #print('holiday name = ',list(country_holidays('US', years=_year_).values())[count]);
              date.append(list(country_holidays('US', years=_year_).keys())[count]);
              count=count+1;
    
    loop_holiday_api(next_year);
    for elements in date:
           #print('type = ',type(elements),'--' ,elements);
           str_elements=str(elements)[5:];
           month=str_elements[:2]
           day=str_elements[3:]
           Month.append(month);
           Day.append(day);
           
    synthetic_cal2=pandas.DataFrame(data);  
    #print('current_month ',current_month)
    full_holiday_set=pandas.concat([synthetic_cal2, holiday_doc], ignore_index=True);
    count_a=0;
    while count_a<len(full_holiday_set['Month']):
        #for stuff in full_holiday_set['Month']:
        #print('reconstructed_date ',reconstructed_date);
        #print("full_holiday_set['Month'] ",type(full_holiday_set['Day'][count_a])," ",full_holiday_set['Month'][count_a]," --  ","full_holiday_set['Day'] type=",type(full_holiday_set['Day'][count_a])," ",full_holiday_set['Day'][count_a]);
        if len(str(full_holiday_set['Month'][count_a]))==2:
            print(full_holiday_set['Month'][count_a]);
            print(str(full_holiday_set['Month'][count_a])[1:]);
        if len(str(full_holiday_set['Day'][count_a]))==2:
            print(full_holiday_set['Day'][count_a]);  
            print(str(full_holiday_set['Day'][count_a])[1:]);
        reconstructed_date.append(str(full_holiday_set['Month'][count_a])+"/"+str(full_holiday_set['Day'][count_a]));
        #print(full_holiday_set['Month'][count_a],full_holiday_set['Day'][count_a]);
        #stringTOdates=datetime.strptime(str(full_holiday_set['Month'][count_a])+"/"+str(full_holiday_set['Day'][count_a]), '%m%d');
        #print(stringTOdates);
        count_a=count_a+1;
    full_holiday_set['reconstructed_date']=reconstructed_date; 
   
    
    '''
    holidays_all_upcomming_months=full_holiday_set[full_holiday_set [Month]>current_month];    
    holidays_upcomming_months=full_holiday_set[full_holiday_set [Month]==current_month+1]; 
    #holidays_soon_next_month=holidays_upcomming_months[holidays_upcomming_months[]];   
    holidays_this_month=full_holiday_set[full_holiday_set [Month]==current_month];
    next_holidays_this_month=holidays_this_month[holidays_this_month[Day]>current_day];   
    holiday_today=holidays_this_month[holidays_this_month[Day]==current_day]; 
    
    print('holidays_all_upcomming_months ',holidays_all_upcomming_months);    
    print('holidays_upcomming_months ',holidays_upcomming_months); 
       
    print('holiday_today ',holiday_today);
    print('next_holidays_this_month ',next_holidays_this_month);
    print('holidays_this_month ',holidays_this_month);   
    '''   
    print(holiday_doc);  
    print(synthetic_cal2);
    print(full_holiday_set);   
    print(datetime.now()+timedelta(days=22));
    print('end holidays');
   
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





