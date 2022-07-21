num = int(input("숫자를 입력해 주세요: "))

if num > 0 :
    if num%2==0:
        print("짝수")
    else :
        print("홀수")

elif num < 0 :
    print("음수")

else :
    print("0")