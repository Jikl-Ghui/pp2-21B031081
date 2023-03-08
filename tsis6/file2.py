import os
path="C:\\Users\\22117\\OneDrive\\OOP\\PP2checker\\text4.txt"
print("Exist: ", os.access(path, os.F_OK))
print("Readable: ", os.access(path, os.R_OK))
print("Writeable: ", os.access(path, os.W_OK))
print("Executable: ", os.access(path, os.X_OK))
