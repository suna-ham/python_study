print(ord('파')) #ord("문자") 문자의 유니코드값 반환
num = ord('파')
print(chr( num))


aa =chr( num+100)


inFp, ouFp =None, None
inStr, outStr = "", ""
i = 0
secu = 0
secuYN = input("1.암호화, 2암호해석")
inFname  = input("입력파일명은?")
outFname =input("출력 파일명은?")
if(secuYN == '1'):
    secu =100
elif(secuYN == '2'):
    secu = -100

inFp = open(inFname, 'r', encoding = 'utf-8')
outFp = open(outFname, 'w', encoding = 'utf-8')
while True :
    inStr = inFp.readline()
    if not inStr :
        break
    outStr =""
    for i in range(0, len(inStr)):
        ch=inStr[i]
        chNum = ord(ch)
        chNum = chNum + secu
        ch2 = chr(chNum)
        outStr = outStr + ch2
    outFp.write(outStr)
outFp.close()
inFp.close()
print(' %s --> %s 변환 완료' % (inFname, outFname))