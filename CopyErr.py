#THIS DOUCMENT TRY TO RECOVER THE DOCUMENTS THAT COULDN'T BE COPIED DUE TO UKNOWN ERROR
import pprint
import os
import shutil
from shutil import copyfile

file = open("/location/to/dump/files/to/CopyErr.txt", "r")
Number = 0
for line in file:
	Number +=1
	fileds = line.split(" || ")
	fullpath = fileds[0]
	newpath = fileds[1]
	newpath = newpath[:-1]
#	print(str(Number) + " Copying " + OldPath + " To " + NewPath)
	if not os.path.exists(newpath):
            	print('Copying ' + newpath)
            	try:
                	os.makedirs(os.path.dirname(newpath), exist_ok=True)
                	#copyfile(fullpath,newpath)
                	shutil.copy2(fullpath, newpath, follow_symlinks=False)              
            	except Exception as e:
            		print(e)
            		#input("Press Enter to continue...")
                	#print('Error copying file ' + fullpath + ' to ' + newpath)
file.close()
Print("Done")
