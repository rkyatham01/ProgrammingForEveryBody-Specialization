#Open file romeo.txt
#Then split the line into a list of words

#You should get a list of words and then check for each word
#that if its already in the list

#Sort the final answer at the end
fname = input("Enter the file name: ")
filehandle = open(fname,"r")

smoflst = list()

for line in filehandle: #Everytime it loops around it gets reset
    line = line.rstrip() #removing white spaces
    line = line.split() #splits at blank spaces
    for x in line: #line is the array here now, x index
        if x not in smoflst: #add if its not in list
            smoflst.append(x)
smoflst.sort() #sorts list by alphabet
#with sort you shouldn't try to = it to something
print(smoflst)