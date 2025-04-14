
digit=int(input("enter the number:"))
count=0
n=abs(digit)
if n==0:
    print("it is 1")
else:
   while n>0:
       n=n//10 
       count=count+1

print("\ncount=",count)
    
