import urllib.request
romeo = urllib.request.urlopen("http://www.py4inf.com/code/romeo.txt").readall().decode('utf8')
romeo = romeo.split()
romeo = set(romeo)
romeo = sorted(romeo)
print(romeo)
