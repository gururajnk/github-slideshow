import sys
user1=input("wt's ur name?")
user2=input("and ur name?")
def use1():
     a=input("%s,do u want to choose rock,paper or scissors?"%user1)
     return(a)
def use2():
    b=input("%s,do u want to choose rock,paper or scissors?"%user2)
    return(b)
def compare(u1,u2):
    if u1==u2:
        return("it is a tie")
    elif u1=='rock':
        if u2=='scissors':
            return("%s,wins!"%user1)
        else:
            return("%s, wins!"%user2)
    elif u1=='scissors':
        if u2=='paper':
            return("%s, wins!"%user1)
        else:
            return("%s, wins!"%user2)
    elif u1=='paper':
        if u2=='rock':
            return("%s, wins!"%user1)
        else:
            return("%s, wins!"%user2)
    else:
        return("invalid syntax,")
        sys.exit()
user1_input=use1()  
user2_input=use2()    
print(compare(user1_input,user2_input))
print("do u want to play another game?")
n=input("enter yes or no:")
while True:
   if n=='yes':
     user1_input=use1()  
     user2_input=use2() 
     print(compare(user1_input,user2_input))
     print('do u want to play one more game?')
     n=input("enter yes or no")
     if n=='yes':
        continue
     else:
        print("game over:!")
        break
   else:
     print("game over!")
     break