import os
path = 'C:\\Users\\22117\\OneDrive\\OOP\\PP2Checker\\text4.txt'
print("Existence test: ")
print(os.path.exists(path))
print("-"*10)
print("Filename:")
print(os.path.basename(path))
print("-"*10)
print("Directory portion:")
print(os.path.dirname(path))