#!/usr/bin/python3
# -*- coding: utf-8 -*
import requests
from bs4 import BeautifulSoup
import datetime
import csv
import os

Basedir = os.path.dirname(os.getcwd())


head= {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

resp= requests.get('http://www.dotamax.com/hero/rate/',headers=head)

soup= BeautifulSoup(resp.text,'lxml')


def get_herolist():
    herolist_class= soup.find_all('span',class_='hero-name-list')
    for item in herolist_class:
        yield item.string


def get_herorate():
    hero_rate_class=soup.find_all('div',class_="segment segment-green")
    for item in hero_rate_class:
        yield float(item['style'][6:-1].strip('%'))



def get_frequency():
    div_=soup.find_all('div',class_="segment segment-gold")
    for item in div_:
        yield int(item.previous_sibling.string.replace(",",""))





if __name__=="__main__":
    AMOUNT = 112
    hero_list= get_herolist()
    hero_rate= get_herorate()
    freq= get_frequency()
    filename=Basedir+'/data/dota2-'+datetime.datetime.now().strftime('%Y%m%d')+'.csv'

    writer =csv.writer(open(filename,'w'))
    writer.writerow(['英雄', '胜率', '使用频率'])
    for index in range(AMOUNT):
        writer.writerow([next(hero_list),next(hero_rate),next(freq)])

        
    # post = {"author": "yzg",
    #     "dota2": "from dotamax",
    #     "tags": ["mongodb", "python", "pymongo"],
    #     "date": datetime.datetime.now().strftime('%Y-%m-%d')}
    #
    # end_id=db['post'].insert_one(post).inserted_id
    # print(end_id)
