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
#If modifying these scopes, delete the file token.json.
#SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]




def holidays_Calendar():
    current_month=datetime.now().month;
    current_day=datetime.now().day;   
       
    #_10_days_from_now=datetime.today() + timedelta(days=10);
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
              date.append(list(country_holidays('US', years=_year_).keys())[count]);
              count=count+1;
    
    loop_holiday_api(next_year);
    for elements in date:
           str_elements=str(elements)[5:];
           month=str_elements[:2]
           day=str_elements[3:]
           Month.append(month);
           Day.append(day);
           
    synthetic_cal2=pandas.DataFrame(data);  
    full_holiday_set=pandas.concat([synthetic_cal2, holiday_doc], ignore_index=True);
    count_a=0;
    while count_a<len(full_holiday_set['Month']):
        alteredDigitMonth=str(full_holiday_set['Month'][count_a]);
        alteredDigitDay=str(full_holiday_set['Day'][count_a]);
        if len(alteredDigitMonth)==1:
            alteredDigitMonth='0'+alteredDigitMonth
        if len(alteredDigitDay)==1:
            alteredDigitDay='0'+alteredDigitDay
        reconstructed_date.append(alteredDigitMonth+"-"+alteredDigitDay);
        count_a=count_a+1;
    full_holiday_set['reconstructed_date']=reconstructed_date; 
    #print('synthetic_cal2');
    #print(synthetic_cal2);
    #print('holiday_doc');
    #print(holiday_doc);
    return full_holiday_set;
   

def Holiday_selector():
    #timedelta(days=10)
    close_holiday=[];
    close_holiday_date=[];
    #upcommingHolidays={'holiday comming up':close_holiday_date,'date':close_holiday_date};
    #upcommingHolidays=pandas.DataFrame({'holiday comming up':close_holiday_date,'date':close_holiday_date});
    
    _today_=str(datetime.today())[5:][:5];
    _today_plus_ten_days=str(datetime.today() + timedelta(days=10))[5:][:5];
    this_month=_today_[:2];
    next_month=str(int(this_month)+1);
    print('this_month = ',this_month);
    print('next_month = ',next_month);
    calendar=holidays_Calendar();
    calendar_dates=calendar['reconstructed_date'];
    #print(holidays_Calendar());
    print('Today = ',_today_);
    counter=0;
    while counter < len(calendar_dates):
       month=calendar_dates[counter][:2];
       the_day=calendar_dates[counter][3:];
       #print('close_holiday_date ',len(close_holiday_date));
       if month==this_month:
           if the_day > _today_[3:]:
              #print('current Month','- date ',the_day);
              #close_holiday.append(calendar['Holiday Name'][counter]);
              #close_holiday_date.append(calendar_dates[counter]);
              print(close_holiday);
              #print(close_holiday_date);
       #print('close_holiday_date ',len(close_holiday_date)); 
       counter=counter+1;
       #print('counter l1= ',counter); 
    if len(close_holiday_date)==0:    
       counter=0;
       while counter < len(calendar_dates):
         month=calendar_dates[counter][:2];   
         #print('counter l2= ',counter);   
         #print(calendar_dates[counter]);  
         print('name - ',calendar['Holiday Name'][counter]);
         #print('month = ',month,'  |  next month = ',next_month);  
         #if len(close_holiday_date)==0:
         if month==next_month:
            print(" name ",calendar['Holiday Name'][counter]); 
            #print('!!!!! month = ',month,'  |  next month = ',next_month);  
            #print('-- under if--',calendar_dates[counter]);  
            #print('-- under if--',calendar['Holiday Name'][counter]);   
            #print('month = ',month,"--",'next_month = ',next_month);
            close_holiday.append(calendar['Holiday Name'][counter]);
            close_holiday_date.append(calendar_dates[counter]);
            #print('broken next month - ',next_month);
            print('name = ',close_holiday); 
            print('date = ',close_holiday_date);    
         counter=counter+1;
    #print(upcommingHolidays)       
    return 0;


Holiday_selector();    



















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





