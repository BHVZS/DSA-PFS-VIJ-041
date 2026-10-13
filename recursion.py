#Recursions
#direct recursion
'''def numbers(n):
    if n==0:
        return
    print(n)
    numbers(n-1)
n=int(input("enter n:"))
numbers(n)'''

#direct recursion - factorial of a number
'''def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n=int(input("enter n:"))
print("Factorial:",fact(n))'''

#Indirect recursion
'''def one(n):
    if n<=0:
        return
    print("one:",n)
    two(n-1)
def two(n):
    if n<=0:
        return
    print("two:",n)
    one(n-1)
n=int(input("enter a number:"))
one(n)'''

#printing even or odd without % using indirect recursion
'''def even(n):
    if n==0:
        print(copy, "is even")
        return
    odd(n-1)
def odd(n):
    if n==0:
        print(copy, "is odd")
        return
    even(n-1)
n=int(input("enter the number:"))
copy=n
even(n)'''

#tree recursion
'''def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
    fun(n-1)
n=int(input("enter the number:"))
fun(n)'''

