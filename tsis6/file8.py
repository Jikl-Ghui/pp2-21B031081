import os
path="C:\\Users\\22117\\OneDrive\\OOP\\PP2Checker\\text.txt" #specific path
try:
    os.remove(path)
except FileExistsError:
    print("File does not exist")
except PermissionError:
    print("You do not have a permission")
else:
    print(path+" has deleted")

