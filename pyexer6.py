word=input("enter the word u want to check it's palindrome property:")
rvs=word[::-1]
print(rvs)    
if word==rvs:
    print("word is palindrome")
else:
    print("word i not palindrome")    
