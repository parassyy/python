sales={2010:45000,
       2011:65000,
       2012:75000,
       2013:85000}
t=0
for y in sales:
    print(y,sales[y])
    t=t+sales[y]
print(t)
