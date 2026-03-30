
# installation of internal module that is the os
import os
# select the directory whose content you want to list
directory_path ='/web development'
# use the os module to list the directory content 
contents = os.listdir(directory_path)
for item in contents:
 print(item)


