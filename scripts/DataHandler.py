import csv
import os
# from scripts.HeroList import HeroNames
from scripts import HeroList



Basedir = os.path.dirname(os.getcwd())
DataDir = Basedir +"/data/"
DataFileList = os.listdir(DataDir)

# defs

# with open(DataDir+'dota2-20161117.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     rows=(row['胜率'] for row in reader)
#     print (list(rows))

# def getfile

class MyHandler(object):


    def __init__(self,filename,*args,**kwargs):
        self.filename=filename
        self.args=args
        self.kwargs=kwargs


    def getRate(self):
        with open(self.filename,'r') as f:
            return [row[HeroList.Column2] for row in csv.DictReader(f)]


    def getFreqency(self):
        with open(self.filename,'r') as f:
            return [row[HeroList.Column3] for row in csv.DictReader(f)]


# if __name__ == "__main__":
#     test=MyHandler(DataDir+'dota2-20161117.csv')
#     print(test.filename)
#     print(test.getFreqency())
#     print(DataFileList)
