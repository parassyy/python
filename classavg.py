class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hey",self.name, "avg is:",sum/3)
s1=student("paras yadav",[90,98,97])
s1.get_avg()

s1.name="ashiwni yadav"
s1.get_avg()
