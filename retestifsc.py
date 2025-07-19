import re
ifsc_code=input("IFSC Code:")
m=re.fullmatch(r'^[A-Z]{4}\d{7}',ifsc_code)
if m!=None:
    print(f'{ifsc_code} is valiD')
else:
    print(f'{ifsc_code} is invalid')
    
