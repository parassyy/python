class  Date: #class definition
    def __init__(self): #constructor
        self.dd=0
        self.mm=0
        self.yy=0
dob=Date()
print(dob.dd, dob.mm, dob.yy)
doj=Date()
print(doj.dd, doj.mm, doj.yy)
doj.dd = 2
doj.mm = 7
doj.yy = 2025
print(doj.dd, doj.mm, doj.yy,sep='/')