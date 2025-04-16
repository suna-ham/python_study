inF, outF = None, None
isStr = ""
inF =open("./python_study/file_inout/temp/data1.txt", "r", encoding="utf=8")
outF =open("./python_study/file_inout/temp/copy_data1.txt", "w", encoding="utf=8")

inList = inF.readlines()
print(inList)
for inStr in inList :
    outF.writelines(inStr)
    
inF.close()
outF.close()