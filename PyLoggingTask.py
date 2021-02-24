# import re
# 183.87.117.45 - - [04/Oct/2018:09:17:54 +0000] 
# "GET /wp-content/themes/twentyseventeen/assets/js/jquery.scrollTo.js?ver=2.1.2 HTTP/1.1" 200 5836 "http://35.154.33.157/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:62.0) Gecko/20100101 Firefox/62.0"
f = open('C:/Users/Vishal Patil/Downloads/access_log','r')

# ls = [1,2,3,4,5,6,7,8]
# print(ls)
alist = []

for line in f:
    tp = int(line.split('"')[2].split(' ')[1])
    alist.append(tp)
    # print(tp)
    # print(line.split('"')[2].split(' ')[1])

# print(alist)
    # print(type(tp))
    # alist.append(tp)

    # print(alist)
    # alist = list(tp)
    # print("elements: " + str(alist))

freq = {}

def countFreq(val):
    for item in val:
        if(item in freq):
            freq[item] +=1
        else:
            freq[item] = 1
    
    # print(freq)
    
    for (key,occ) in freq.items():
        # print(str(key)+ " " )
        print("Status code "+ str(key)+ "-> count "+ str(occ))

countFreq(alist)