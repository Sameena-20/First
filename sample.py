n=int(input("Enter the number:"))
s=0
r=0
while(n>0):
    d=n%10
    s=s+d
    r=r*10+d
    n=n//10
print("Sum of digits:",s)
print("________Updated part of the code_______")
print("Reverse the number:",r)
