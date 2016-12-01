
import pymongo
import requests
import os


client = pymongo.MongoClient(host="127.0.0.1", port=27017)
db = client['test_cw']
result=db['dota_hero'].find({},{'url':1,"_id":0})
url_list = [b['url'] for b in list(result)]


# print(url_list.__len__())
url_file = os.path.dirname(os.getcwd())+"/static/url.txt"


def Downloader():

    if not os.path.exists(url_file):
        for url in url_list:
            print(url)
            with open(url_file, 'a') as f:
                f.write(url + "\n")

    for url in url_list:
        name=url.split("/")[-1]##.split("_")[1]+".png"
        download_file=os.path.dirname(os.getcwd())+"/static/images/"+name
        if not os.path.exists(download_file):
            r = requests.get(url, stream=True)
            print(r.url)
            with open(download_file,'wb') as f:
                f.write(r.content)
            print("%s download OK!"%name)



if __name__ == "__main__":
    Downloader()