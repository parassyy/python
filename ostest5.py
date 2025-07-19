import os.path
fname=input("Filename to find:")
if os.path.exists(fname):
    print(f'{fname} found')
else:
    print(f'{fname} not found')
    
