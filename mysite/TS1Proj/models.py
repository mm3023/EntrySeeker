import requests;
import json
import pandas

def zeist_initiate():
    print("zeist is online");
    return 0;
zeist_initiate();

def JsonRequestResolver1(x):
        test_for_string=type(x);
        if type(x)=="<class 'str'>":
            print("string confirmed");
        else:
            print('string expected');
        print(type(x));
        print(type(test_for_string));
    
        #x is the URL appropriately structured;
        response=requests.get(x).json();
        resFrame=pandas.DataFrame(response);
        reFrame=[item.split(",") for item in resFrame];
        return reFrame;

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
"""
response2 = requests.get('https://date.nager.at/api/v3/PublicHolidays/2024/US')
res2=response2.json();
res2=json.loads(res2);
#response_2=pandas.read_json(response2[1]);
#response_2=pandas.read_json(response2);
print('');
"""



