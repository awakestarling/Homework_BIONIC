f = open('mbox-short.txt','rt')
w = open('mbox-short-upper.txt', 'w')
for line in f.readlines():
    w.writelines(line.upper())
f.close()
w.close()
