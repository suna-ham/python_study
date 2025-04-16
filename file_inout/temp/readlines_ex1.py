inF = None
inStr = ""
# print(type(inF))
# print(type (inStr))

inF = open("./python_study/file_inout/temp/data1.txt", "r", encoding="utf=8")
inStr = inF.readlines()
print(inStr)

inF.close()

with open("./python_study/file_inout/temp/data1.txt", "r", encoding="utf=8") as inF:
    inStr=inF.read()
    print(inStr)