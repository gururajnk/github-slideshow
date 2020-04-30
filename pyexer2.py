print("enter ur number:")
x=int(input())
if x%2==0:
    if x%4==0:
        print("the number is multiple of 4:",x)
    else:
        print("the no. is only multiple of 2:",x)
else:
    print("the no. is odd and it is",x)