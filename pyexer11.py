print("enter two numbers for primity check:")
def primeity(i):
    count=0
    for x in range(1,i+1):
       if i%x==0:
         count=count+1
       else:
         count=count
    if count>2:
       return("i is not a prime no.")
    else:
       return("input is prime no:")
def number(n):
    return(int(input(n))) 
fn=number("first no.:")
sn=number("second no.:")
print(primeity(fn))
print(primeity(sn))
