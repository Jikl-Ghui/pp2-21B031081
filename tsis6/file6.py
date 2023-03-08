import os
str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

directory = os.getcwd()
if not os.path.exists('26 texts'):
    os.mkdir('26 texts')

new_path = path = os.path.join(directory, '26 texts')
os.chdir(new_path)

for i in str :
    with open(f'{i}.txt', 'a') as f :
        f.write(i)