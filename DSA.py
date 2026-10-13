

            #DSA
#write a program to add thr digits of a given number
'''n=int(input("enter thr number:"))
s=0
while n!=0:
    d=n%10
    s+=d
    n//=10
print("sum:",s)'''  

#write a program to reverse a given nuumber without using reverse
'''n=int(input("enter the number:"))
while n!=0:
    d=n%10
    print(d, end=" ")
    n//=10'''

#2nd method write a program to reverse a given number
'''n=int(input("enter the number:"))
rev=0
while n!=0:
    d=n%10
    rev=(rev*10)+d
    n//=10
print(rev)'''

#generate n even numbers
'''n=int(input("enter the number:"))
i=1
while i<=n:
    if i%2==0:
        print(i,end=" ")
    i+=1   '''

#natural numbers
'''n=int(input("enter n:"))
for i in range(1,n+1):
    if i%2==1:
        print(i,end=" ")'''

#2-D data square pattern with numbers
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        print(j,end=" ") for printing j
    print()'''

'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        print(i,end=" ") printing i
    print()'''
    

'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        print("*",end=" ") for printing *
    print()'''

#2-D data Hollow square pattern with numbers
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() '''

#2-D data hollow pattern with * diagonal prints intersection
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
         if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
            print("*",end=" ")
         else:
            print(" ",end=" ")
    print()'''

#2-D data hollow pattern with * hourglass
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
         if i==0 or i==n-1 or i==j or i+j==n-1:
            print("*",end=" ")
         else:
            print(" ",end=" ")
    print()'''

#2-D data hollow pattern with * intersection at the middle
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==n//2 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() '''

#2-D data hollow square pattern * with * in middle
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1 or i==n//2 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''


#2-D pattern printing by removing above 1st row and last row  
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
         if j==0 or j==n-1 or i==j or i+j==n-1:
            print("*",end=" ")
         else:
            print(" ",end=" ")
    print() 
'''


#2-D pattern pattern removing sides
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
         if i+j==n-1 or i==j:
            print("*",end=" ")
         else:
            print(" ",end=" ")
    print() '''


#2-D printing +
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() '''


