import glob
import time

#Now=time.strftime("%b %d %Y  %H:%M:%S")
#print(Now)
#filespath=glob.glob("*.txt")
#print(filespath)
filepaths=glob.glob("files/*.txt")
for filepath in filepaths:
    with open(filepath,'r') as file:
        print(file.read())