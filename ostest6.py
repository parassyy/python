import os.path
fname=input("filename:")
if os.path.exists(fname):
    if os.path.isfile(fname):
        size=os.path.getsize(fname)
        print(f'{fname} size in bytes is {size}')
    else:
        print(f'{fname} not regular file')

else:
    print(f'{fname} not found')
