import os
directory="C:\\Users\\22117\\Documents"
choice=int(input("\n1-directories \n2-files and directories \n3-files \n"))
for i in os.listdir(directory):
    path=os.path.join(directory,i)
    if choice==1 or choice==2:
        if os.path.isdir(path):
            print(f'Dir:{i} ')
            if choice ==2:
                for i2 in os.listdir(path):
                    print('-'*6,i2)
    else:
        if os.path.isfile(path):
            print(f"File:{i} ")
