print("number to which divisors are required:")
n=int(input())
x=range(1,n+1)
divisors=[]
for elem in x:
    if n%elem==0:
        divisors.append(elem)
    else:
        pass

print(divisors)    