print("***Menu***")
print("1.area of circlr")
print("2.area of trangle")
print("3.area of rectangel")
print("4.Exit")
opt=int(input("enter the option you want:"))
match(opt):
    case 1:
        r=float(input("enter the radius:"))
        r=3.14*r*r
        print("area of cirlcr is:",r)
    case 2:
        bc=float(input("enter the base of tri"))
        h=float(input("enter the heiht of tri"))
        t=0.5*bc*h
        print("area of trinagle is:",t)
    case 3:
        l=float(input("enter the length:"))
        b=float(input("enter the bradth:"))
        ar=l*b
        print("area of rectangle is:",ar)
    case _:
        print("invalid opt try agin")
        
