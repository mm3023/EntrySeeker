import requests;
import json
import pandas
from datetime import datetime




def zeist_initiate():
    print("zeist is online");
    return 0;
zeist_initiate();

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




#now=datetime.now();
#print(datetime.now());

def open_holiday_DataFrame():
    print('open_holiday_DataFrame;-called');
    print(type(datetime.now()));
    #print('datetime.now()');
    print(datetime.now());
    dateString=datetime.now().strftime("%Y-%m-%d %H:%M:%S");
    print('type(dateString)');
    print(type(dateString));
    print(dateString[10]);
    print(dateString);
    print('open_holiday_DataFrame;-end');
open_holiday_DataFrame();
     

open_holiday_set=JsonRequestResolver1('https://openholidaysapi.org/PublicHolidaysByDate?languageIsoCode=DE&date=2023-12-25');   
print(open_holiday_set)    



print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::");
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::");

#nager api alter year/country code;
#https://date.nager.at/api/v3/PublicHolidays/2024/US

date_nager_at=JsonRequestResolver1('https://date.nager.at/api/v3/PublicHolidays/2024/US');

print(date_nager_at);
print('-------------------------------------------')
open_holiday_DataFrame();
open_holiday_DataFrame();



