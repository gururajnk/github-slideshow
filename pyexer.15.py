s=input("enter the string:")
result=s.split()
n=len(result)
newresult=[]
for i in range(0,n):
    item=result[n-i-1]
    newresult.append(item)
    
print(newresult)   
    
result1=" ".join(newresult)
print(result1)