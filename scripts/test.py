import os
url_file = os.path.dirname(os.getcwd())+"/static/url.txt"


url_list =[]
if os.path.exists(url_file):
    with open(url_file,'r') as f:
        for line in f:
            url_list.append(line.strip())


print(url_list)
