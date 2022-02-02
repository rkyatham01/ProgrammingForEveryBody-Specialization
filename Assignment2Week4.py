#Parsed From line using split()
#print the email for each one and included
# a count at the end

fname = input("Enter file name : ")
if (len(fname) < 1): #Default if empty typed in
    fname = "mbox-short.txt"

filehndlr = open(fname,"r")
count = 0

for line in filehndlr:
    line = line.rstrip()
    if line.startswith("From "): #if it starts with something do this
        line = line.split()
        print(line[1]) #prints the email out
        count = count + 1 #increases count by 1

print("There were",count,"lines in the file with From as the first word")