import os
import sys

dir1, dir2,file_name = sys.argv[1:]
list_files = os.listdir(dir1)
res = ''
for i in range(len(list_files)):
    res+=f'{dir1}/{list_files[i]} {dir2}/{list_files[i]}\n'
f = open(file_name,'w')
f.write(res)
f.close()