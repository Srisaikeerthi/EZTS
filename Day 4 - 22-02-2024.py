#PROGRAM-1 - pangram hacker rank
#APPROACH-1
s=input()
s1=set(s)
if len(s1) == 27:
    print("pangram")
else:
    print("not a pangram")


#APPROACH-2
alpha={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
s=input()
d={}
for i in s:
    if i in alpha:
        if i not in d;
            d[i]=1
        else:
            d[i]+=1
x=d.keys()
print(d)
if len(x) == 26:
    print("pangram")
else:
    print("not a pangram")



#PROGRAM-2 -first repeating character
t = int(input())
for i in range(t):
    s = input()
    d = {}
    for i in s:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    for i in d:
        if d[i] == 2:
            print(i)
            break
    else:
        print(".")



#PROGRAM-3 -dict and map
n=int(input())
d={}
for i in range(n):
    name,number=input().split()
    d[name]=number
while(1):
    s=input()
    if s in d:
        print(f"{s}={d[s]}")
    else:
        print("not found")
    


#PROGRAM-4 -most frequent
n=int(input())
d={}
for i in range(n):
    s=input()
    if s in d:
        d[s]=d[s]+1
    else:
        d[s]=1
x=max(d.value())
z=[]
for i in d:
    if d[i]==x:
        z.append(i)
print(max(z),x)




#PROGRAM-5 -database
t=int(input())
for i in range(t):
    n,r=map(int,input().split())
    d={}
    for j in range(r):
        sid=cid=map(int,input().split())
        if cid not in d:
            d[cid]=[sid]
        else:
            d[cid].append(sid)
     #print(d)
    for j in d:
        if len(d[j])>n and len(set(d[j])) == len(d[j]):
            print(f"Scenario #{i+1} : Impossible")
            break
    else:
        print(f"Scenario #{i+1} : Possible")



# PROGRAM-6 -directed unweighted graph
n=int(input())
route={}
for i in range(n):
    c1,c2=input().split()
    if c1 not in route:
        route[c1]=[c2]
    else:
        route[c1].append(c2)
print(route)
city=input()
if city in route:
    print(*route[city],sep=" ")
else:
    print("None")


    