#Open and read Log file
f = open('C:/Users/Vishal Patil/Downloads/access_log','r')

#Creating a list to store classified data
alist = []

# iterating over all lines and extracting error code
for line in f:
    tp = int(line.split('"')[2].split(' ')[1])
    alist.append(tp)
    
#creating empty dictionary to store key value pair as (error : count)
freq = {}

#creating function to count occurances of individual element
def countFreq(val):
    for item in val:
        if(item in freq):
            freq[item] +=1
        else:
            freq[item] = 1
    
    
    for (key,occ) in freq.items():
        print("Status code "+ str(key)+ "-> count "+ str(occ))

        
countFreq(alist)
