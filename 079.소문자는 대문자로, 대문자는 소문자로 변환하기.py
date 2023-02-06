#아스키코드값 사용
letter=input()
result=''
for l in letter:
    if 65<= ord(l) <=90 :       
        result += chr(ord(l)+32)
    elif 97<= ord(l) <=122 :
        result += chr(ord(l)-32)
    else:  #공백, 특수기호, 마침표 등
        result+=l
print(result)  


#isupper, islower 사용
letter=input()
result=''

for l in letter:
    if l.isupper()==True :      
        result += chr(ord(l)+32)
    elif l.islower()==True :
        result += chr(ord(l)-32)
    else:  #공백, 특수기호, 마침표 등
        result+=l
print(result)  




   