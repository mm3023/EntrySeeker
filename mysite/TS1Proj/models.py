import requests;
import json
import pandas

def zeist_initiate():
    print("zeist is online");
    return 0;
zeist_initiate();

#response = requests.get('https://api.github.com/user', auth=('user', 'pass'))
#https://openholidaysapi.org/PublicHolidaysByDate?languageIsoCode=DE&date=2023-12-25
response = requests.get('https://openholidaysapi.org/PublicHolidaysByDate?languageIsoCode=DE&date=2023-12-25');
res1=response.json();
print(res1.keys());
print(res1[0]);
print(res1[1]);
"""
print(res1"[0][0]");
print(res1[0][0]);
print("res1[0][1])";
print(res1[0][1]);
"""      
#res1=json.loads(res1);

#response1=open(response);
#response1=json.load(response1);


#print(response1);
"""

#print(response1)[1];
#pandas.read_json(response1);

#response_1=pandas.read_json(response1);
#print(response_1);
"""

print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::");
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::");
"""
#nager api alter year/country code;
#https://date.nager.at/api/v3/PublicHolidays/2024/US
response2 = requests.get('https://date.nager.at/api/v3/PublicHolidays/2024/US')
res2=response2.json();
res2=json.loads(res2);
#response_2=pandas.read_json(response2[1]);
#response_2=pandas.read_json(response2);
print('');
"""



