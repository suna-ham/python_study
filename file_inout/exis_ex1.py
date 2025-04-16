import os

inFp = None
fName = ""
inList = []
inStr = ""

fName = input( '파일명을 입력에요')
if(os.path.exists(fName)):
    with open(fName, "r") as inFp :
        if os.path.exists(fName) :
    inFp = open(fName, "r")
    
    inList = inFp.readlines()
    for inStr in inList :
        print(inStr, end = "")
        
    inFp.close()
\