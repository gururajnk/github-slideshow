import random
a=[]
b=random.randint(5,15)
while len(a)<b:
    a.append(random.randint(1,75))
    
evenlist=[x for x in a if x%2==0]    
print(a)
print(evenlist)