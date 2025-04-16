
inF= None #자료형이 무엇인지 정해지지 않았을때 사용

inF = open("./python_study/file_inout/temp/data1.txt", "r", encoding="utf-8")
while (True):
    inStr = inF.readline()
    if inStr == "": #참이면EOF(end of file)
        break
    else:
        print(inStr)

inF.close()

data2 = open("./python_study/file_inout/temp/data2.dat", "r", encoding="utf-8")
while(True):
    indata2 = data2.readline()
    if indata2 == "":
     break
    else:
       print(indata2)
data2.close()