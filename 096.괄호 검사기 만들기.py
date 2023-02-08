n = input('괄호의 자료를 입력하세요:')
def makit(n):
    if n[0] == ')':
        return False
    
    num1=0
    num2=0
    for i in range(len(n)):
        if n[i]=='(':
            num1+=1
        elif n[i]==')':
            num2+=1    
    
    if num1==num2:
        return True
    else:
        return False

if makit(n): # 괄호 검사 함수 호출
    print('성공')
else:
    print('실패')