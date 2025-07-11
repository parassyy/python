p=set()
n=int(input("how may playerrs you added:"))
for i in range(n):
    name=input()
    p.add(name)
for name in p:
    print(name)
print(p)
