from bs4 import BeautifulSoup
from seleniumpython import *
import re

source = scrap("https://www.un.org/securitycouncil/content/un-sc-consolidated-list")
soup = BeautifulSoup(source,'lxml')

un = []

full_data = soup.find('table',{'class' : 'display'})
row_data = full_data.find_all('tr',{'class':'rowtext'})
for data in row_data:
    if data and data is not None:
        spliting_data = data.text.strip().split('\xa0')
        name_list = re.findall('\w*\S\w',str(spliting_data[1]))
        name_data = name_list[1] + name_list[2] + name_list[3]
        spliting_data = data.text.strip().split('\xa0',2)
        title_data = re.findall('\S+',str(spliting_data[1]))[-1]
        spliting_data = data.text.strip().split('\xa0',3)
        designation_data = spliting_data[2].split(': ')
        spliting_data = data.text.strip().split('\xa0',4)
        dob_data = spliting_data[3].split(': ')
        spliting_data = data.text.strip().split('\xa0',5)
        pob_data = spliting_data[4].split(': ')
        spliting_data = data.text.strip().split('\xa0',6)
        good_quality_data = spliting_data[5].split(': ')
        spliting_data = data.text.strip().split('\xa0',7)
        low_quality_data = spliting_data[6].split(': ')
        spliting_data = data.text.strip().split('\xa0',8)
        nationality_data = spliting_data[7].split(':  ')
        spliting_data = data.text.strip().split('\xa0',9)
        passport_data = spliting_data[8].split(": ")
        spliting_data = data.text.strip().split('\xa0',10)
        national_identify_data = spliting_data[9].split(': ')
        spliting_data = data.text.strip().split('\xa0',11) 
        address_data = spliting_data[10].split(': ')
        spliting_data = data.text.strip().split('\xa0',12) 
        listed_on_data = spliting_data[11].split(': ')
        spliting_data = data.text.strip().split('\xa0',13)
        other_info_data = spliting_data[12].split(': ')

    Data = {
    "Name" : name_data,
    "Title" : title_data,
    "Designation" : designation_data[1], 
    "Day of birth" : dob_data[1],
    "Place of birth" : pob_data[-1],
    "Good quality a.k.a" : good_quality_data[-1],
    "Low quality a.k.a" : low_quality_data[-1],
    "Nationality" : nationality_data[-1],
    "Passport no" : passport_data[-1],
    "National identification no" : national_identify_data[-1],
    "Address" : address_data[-1],
    "Listed on" : listed_on_data[-1],
    "Other information" : other_info_data[-1]
    }
    un.append(Data)
print(un[0:2])
        
