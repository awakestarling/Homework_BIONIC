
str = 'X-DSPAM-Confidence:  0.8475'
a = str[str.find(' ')+1:]
a = float(a)
print(a)