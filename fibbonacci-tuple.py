
def make_fibonacci(n):
    fib=[]
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
        fib.append(a)
    print(tuple(fib))
n=int(input("enter the number of terms for fibonacci serires:"))
make_fibonacci(n)
