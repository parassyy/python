def li(list,idx=0):
    if idx==len(list):
        return

    print(list[idx])
    li(list,idx+1)
a=list(range(10,60,10))
li(a)
