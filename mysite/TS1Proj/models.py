import requests;
import json
import pandas

def zeist_initiate():
    print("zeist is online");
    return 0;
zeist_initiate();

#response = requests.get('https://api.github.com/user', auth=('user', 'pass'))
#https://openholidaysapi.org/PublicHolidaysByDate?languageIsoCode=DE&date=2023-12-25
response1 = requests.get('https://openholidaysapi.org/PublicHolidaysByDate?languageIsoCode=DE&date=2023-12-25').json();

response_1=pandas.read_json(response1);
print(response_1);

print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::");
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::");

#nager api alter year/country code;
#https://date.nager.at/api/v3/PublicHolidays/2024/US
response2 = requests.get('https://date.nager.at/api/v3/PublicHolidays/2024/US').json();
response_2=pandas.read_json(response2);
print(response_2);




