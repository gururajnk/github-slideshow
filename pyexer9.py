import random
x=random.randint(0,10)
def use():
  userinput=int(input("enter input:"))
  return(userinput)
def compare(u):
  if x==u:
     return("exactly right guess!")
  elif x-u>0 and x-u<5:
      return("guess was closer")
  elif x-u>0 and x-u>5:
      return("guess was too wide")
  elif u-x>0 and u-x<5:
      return("guess was closer")
  elif u-x>0 and u-x>5:
      return("guess was too wide")
  else:
      pass
u1=use()
print(compare(u1))
print("do u want to continue guessing?")
ans=input('enter yes or exit:')
m=1
while True:
    if ans =='yes':
        u1=use()
        print(compare(u1))
        m=m+1
        print("do u want to play one more game?")
        ans=input("enter yes or exit:")
        if ans=='yes':
            continue
        else:
            print('game of guessing is over ')
            break
    else:
        print("game over")
        
        break

print("total no of guessing :",m)     