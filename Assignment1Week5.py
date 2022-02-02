#reads through mbox-short.txt
#figure out who sent the greatest number of mail messages
#looks for From Lines, takes the second word of those lines
#maps the senders mail address to the count of the # of times they appear in file
#Then find maximum loop to find most profilic commiter

file = input("Enter file : ")
if len(file) < 1: #default while if nothing is inputted in
    file = "mbox-short.txt"

filehndlr = open(file, "r") #puts it in read mode
dictionary = dict() #creates empty dictionary

for line in filehndlr:
    line = line.rstrip() #just in case remove the spaces at the end
    if line.startswith("From "):
        line = line.split() #splits the thing at the spaces
        email = line[1]
        if email not in dictionary:
            dictionary[email] = 1
        else:
            dictionary[email] = dictionary[email] + 1

#Here we find the most profilic commiter
bigCount = None
bigWord = None

for keys,val in dictionary.items(): #key value serve for items
    #dictionaries are random but these correspondense isn't to items
    if (bigCount is None) or (val > bigCount):
        bigCount = val
        bigWord = keys
print(bigWord,bigCount)
