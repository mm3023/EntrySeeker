import requests;
import json
import pandas
from datetime import datetime




def zeist_initiate():
    print("zeist is online");
    return 0;
zeist_initiate();

def JsonRequestResolver1(x):
        test_for_string=type(x);
        if type(x)==type('x'):
            print("string confirmed");
        else:
            print('string expected')
            return'string expected';
        print(type(x));
        print(type(test_for_string));
    
        #x is the URL appropriately structured;
        response=requests.get(x).json();
        resFrame=pandas.DataFrame(response);
        #reFrame=[item.split(",") for item in resFrame];
        
        return reFrame;




#now=datetime.now();

open_holiday_DataFrame:
    nowdatetime.now();
    print(now);
open_holiday_DataFrame;
     

open_holiday_set=JsonRequestResolver1('https://openholidaysapi.org/PublicHolidaysByDate?languageIsoCode=DE&date=2023-12-25');   
print(open_holiday_set)    



print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::");
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::");
"""
#nager api alter year/country code;
#https://date.nager.at/api/v3/PublicHolidays/2024/US
"""
date_nager_at=JsonRequestResolver1('https://date.nager.at/api/v3/PublicHolidays/2024/US');

print(date_nager_at);
open_holiday_DataFrame;



