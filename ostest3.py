import os

folder_name=input("Folder name to delete:")
try:
    os.rmdir(folder_name)
    print("folder is deleted..")
except:
    print("folder is not empty cannot delete")
