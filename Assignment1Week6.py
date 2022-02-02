#Get the hour of the day and then split the string again
#Accumulate the counts for each hour
#Then print out the counts and sort by the hour

file = input("Enter a file here: ")

if len(file) < 1:
    file = "mbox-short.txt"

filehndler = open(file,"r")
dictionary = dict() #creates an empty dictionary

for line in filehndler:
    line = line.rstrip()
    if line.startswith("From "):
        line = line.split() #Splits it once
        stores = line[5] #stores the full time in stores
        stores = stores.split(":") #uses a delimiter to split by ":"
        time = stores[0] #has the time
        if time not in dictionary:
            dictionary[time] = dictionary.get(time,1) #puts it in the dictionary as count 1
        else:
            dictionary[time] = dictionary[time] + 1 #increases count by 1 of the hours


NewList = sorted([(key,value) for (key,value) in dictionary.items()]) #sorts and reverses the list of tuples
for lines in NewList:
    print(lines[0], lines[1])



