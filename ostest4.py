import os

folder_name=input("folder name:")
try:
    list1=os.listdir(folder_name)
    print(list1)
    print(len(list1))
except:
    print("invalid foldername")
