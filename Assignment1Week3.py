
#Prompts file for a given name and opens it
#Then it reads through the file and prints the contents oof the file in upper case

fname = input("Enter file name: ") #enter the file name here
filehndler = open(fname,"r") #filehndler creates a portal sort of to the data of the file

for line in filehndler:
    reline = line.upper() #makes every line in file uppercase
    reline = reline.rstrip() #here we have to rstrip because it is doing \n twice
    print(reline)