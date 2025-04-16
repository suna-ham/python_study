inF, outF = None, None
isStr = ""
inF =open("./python_study/file_inout/temp/pyimg.jpg", "rb") #img는 이진법!
outF =open("./python_study/file_inout/temp/pyimg_copy1.jpg", "wb")

for i in inF.readlines():
    outF.write(i)
inF.close()
outF.close()