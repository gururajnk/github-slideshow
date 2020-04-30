print("enter ur two numbers:")
num=int(input())
check=int(input())
if check%num==0:
    print("check is evenly divided into num:")
    x=check/num
    print("check is divided into",x,"parts")
else:
    print("check is not divided evenly into num")