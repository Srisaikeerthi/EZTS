#PROGRAM 1 - check whether python is call by value or call by reference
def myfun(x):
    x[0]=20
lst=[10,11,12,13,14,15]
myfun(lst)
print(lst)




#PROGRAM 2 - sugarcane juice business

#APPROACH - 1
t=int(input())
for i in range(t):
    n=int(input())
    i=50*n
    #j=20/100
    #k=20/100
    #l=30/100
    res=i-(70/100)*i
    print(int(res)) 


#APPROACH - 2
t=int(input())
while t>0:
    n=int(input())
    x=n*50-(0.7*50*n)
    print(x)
    t=t-1


#APPROACH - 3
t=int(input())
def test(t):
    if t>0:
        n=int(input())
        x=n*50-(0.7*50*n)
        print(x)
        t=t-1
    else:
        return
    test(t-1)
test(t)


#APPROACH - 4
t=int(input())
def profit(n):
    x=int(n*50-(0.7*50*n))
    return x
def test(t):
    'test(t-1)' # iinfinite test
    if t>0:
        n=int(input())
        print(profit(n))
    else:
        return
    test(t-1)
test(t)




#PROGRAM 3 - watching movies at 2x -  movie2x

#APPROACH - 1
x,y=map(int,input().split())
k=x-y
k1=k-(y//2)
print(k1)
#print(int(x-(y/2)))


#APPROACH - 2
def ans(x,y):
    z=(x-y)+(y//2)
    print(z)
a,b=map(int,input().split())
ans(a,b)


    

#PROGRAM 4 - luckfour

#APPROACH - 1
t=int(input())
for i in range(t):
    n=int(input())
    count=0
    while(n>0):
        if n%10==4:
            count+=1
        n=n//10
    print(count)


#APPROACH - 2
t=int(input())
def ans(n):
    count=0
    while(n>0):
        if n%10==4:
            count+=1
        n=n//10
    return count
def test(t):
    if t>0:
        n=int(input())
        print(ans(n))
    else:
        return
    test(t-1)
test(t)




#PROGRAM 5 - si basic compute n hacker rank

#APPROACH - 1
n=int(input())
r=1
for i in range(1,n+1):
    r=r*i
print(r)


#APPROACH - 2
n=int(input())
r=1
while n>0:
    r=r*n
    n=n-1
print(r)


#APPROACH - 3
k=int(input())
def fact(n):
    if(n==0)or(n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(k))





#PROGRAM 6 - next even integer
n=int(input())
if n%2==0:
    print(n+2)
else:
    print(n)
    

#PROGRAM 7 - append 3 at starting and ending of the integer

#APPROACH - 1
n=int(input())
n=n/1000
n=n+3
n=n*1000
n=(n*10)+3
print(n)


#APPROACH - 2
n=int(input())
n=(n*10)+3
rev=0
while(n>0):
    rev=rev*10 + (n%10)
    n=n//10
rev=(rev*10)+3

final=0
while(rev>0):
    final=final*10 + (rev%10)
    rev=rev//10
    print(rev)
