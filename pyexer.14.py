print("This is a progamm to input a list and return a new list without duplicates: ")
num=int(input("no of elements want to enter ?"))
list=[]
for i in range(0,num):
    x=int(input())
    list.append(x)
    
print(list)
newlist=set(list)
print(newlist)