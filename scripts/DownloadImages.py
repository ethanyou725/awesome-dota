
import pymongo
import requests
import os


client = pymongo.MongoClient(host="127.0.0.1", port=27017)
db = client['test_cw']
result=db['dota_hero'].find({},{'url':1,"_id":0})
url_list = [b['url'] for b in list(result)]
EName=[]


for url in url_list:
    name = url.split("/")[-1].split("_")[0] + ".png"
    EName.append(name)

def Downloader():
    for url in url_list:
        name=url.split("/")[-1].split("_")[0]+".png"
        r=requests.get(url,stream=True)
        with open(os.path.dirname(os.getcwd())+"/static/images/"+name,'wb') as f:
            f.write(r.content)
            print("%s download OK!"%name)



if __name__ == "__main__":
    Downloader()