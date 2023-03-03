import time
current_time=time.localtime()
dmy=time.strftime("%d %m %Y",current_time)
new_dmy=dmy.split()
new_dmy[0]=int(new_dmy[0])-5
if new_dmy[0]<0:
    new_dmy[1]=int(new_dmy[1])-1
    if new_dmy[1]<0:
        new_dmy[2]=int(new_dmy[2])-1
print(dmy)
print(str(new_dmy[0]) +" "+new_dmy[1]+" "+new_dmy[2])
#done
