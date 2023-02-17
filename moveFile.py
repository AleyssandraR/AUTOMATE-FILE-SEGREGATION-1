import os

from_dir='C:/Users/user/OneDrive/Desktop'

isExist=os.path.exists(from_dir)
print(isExist)

list_of_files=os.listdir(from_dir)
print(list_of_files)