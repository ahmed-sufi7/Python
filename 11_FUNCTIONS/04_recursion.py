 # fibonacci series 0 1 1 2 3 5 8 13 21 34
#                   0 1 2 3 4 5 6 7 8 9 10

'''
fib(0)=0
fib(1)=1
fib(2)=fib(0)+fib(1)
fib(3)=fib(1)+fib(2)
fib(4)=fib(2)+fib(3)
fib(n)=fib(n-1)+fib(n-2)
'''
n = int(input("Enter the value of n: "))
def fib(n):
    #base case for recursion
    if(n==0 or n==1):
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(n))