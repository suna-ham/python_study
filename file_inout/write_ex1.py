outF = None
outStr = ""
fName = input("출력할 파일명을 입력하세요")
outF = open(fName, "a", encoding="utf=8")
while(True): 
    outStr = input("정장할 내용을 키보드로 입력?")
    if(outStr != ""):
        outF.writelines(outStr + "\n")
    else:
        break

outF.close()
print("파일이 저장되었습니다")

