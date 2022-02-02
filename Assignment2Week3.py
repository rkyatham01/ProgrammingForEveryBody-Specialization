
fname = input("Enter file name:")

filehandler = open(fname, "r")
smofanswer = 0
Secondvariable = 0
count = 0

for line in filehandler:
    if line.startswith("X-DSPAM-Confidence:"):
        Secondvariable = float(line[19:])#finds the decimal float
        smofanswer = ((Secondvariable + smofanswer)) #Finds the sum of the values
        count = count + 1

answer = (smofanswer/count) #gets the average of the values
print("Average spam confidence:", answer)
