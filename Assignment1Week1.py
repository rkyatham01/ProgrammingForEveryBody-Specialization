#String Manipulation

text = "X-DSPAM-Confidence:    0.8475"
x = text.find("0") #finds where 0 is index
reformattedtext = text[x:x+6]
inttext = float(reformattedtext)

print(inttext)
