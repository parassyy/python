import os

folder_name=input("Folder name:")
try:
    os.mkdir(folder_name)
    print('folder creted')
except:
    print('Error in creaing..')
