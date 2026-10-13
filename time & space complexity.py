
#time complexity and space complexity
#O(1)- constant time complexity space complexity=O(1)
'''n=int(input("enter a number:"))
print(n+100)

#O(n)-linear time complexity space complexity O(1)
n=int(input("enter number:"))
for i in range(1,n+1):
    print(i,end=" ")'''

#O(n)-linear time complexity linear space compelxity O(1)
'''n=int(input("enter number:"))
arr=[]
for i in range(n):
    num=int(input("enter number:"))
    arr.append(num)
print("list",arr)'''

#O(n^2) quadratic TC
'''n=int(input("enter n:"))
num=1
for i in range(n):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()  '''

#logarthmic TC O(log(n))
'''n=int(input("enter a value:"))
while n>1:
    print(n)
    n//=2
print(1)'''

#logarthmic TC O(n(log n))
n=int(input("enter n:"))
for i in range(n):
    j=n
    while j>1:
        j//=2
print("Done")        


