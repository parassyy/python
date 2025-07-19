import csv 
fobj=open("product.csv","a",newline='')
dwobj=csv.DictWriter(fobj, fieldnames=['pname','price'])
dwobj.writeheader()
while True:
    pname=input("ProductName:")
    price=int(input("Price:"))
    prod={'pname':pname,'price':price}
    dwobj.writerow(prod)
    ans=input("add another product?")
    if ans=="no":
        break
fobj.close()
