n=int(input("Enter total participants: "))
for i in range(n+1):
    x=list(map(int,input("Enter their position: ").split(" ")))
    y=set(x)
    z=list(y)
    z.sort()
    break
print("The runner up is", z[-2])