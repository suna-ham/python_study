inF, outF = None, None
isStr = ""
inF =open("./python_study/file_inout/temp/video_a.mp4", "rb") #img는 이진법!
outF =open("./python_study/file_inout/temp/video_a_copy.mp4", "wb")

while(True):
    i = inF.read()#한글자씩 읽어
    if (i == ""):
        break
    else:
        outF.write(i)
inF.close()
outF.close()