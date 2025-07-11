def find_power(num):
    def power(p):
        r=num**p
        return r
    return power
pow2=find_power(5)
res1=pow2(3)
print(res1)
pow4=find_power(4)
res2=pow4(5)
res3=pow4(3)
print(res2,res3)
