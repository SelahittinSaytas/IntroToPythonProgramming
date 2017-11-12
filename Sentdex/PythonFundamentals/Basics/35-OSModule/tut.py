import os

##OS for any sorts of directory operations
##Changing your path
##Making directories or folders
##Deleting them - moving them around
##To move directories - rename directories

curDir = os.getcwd() ##'cwd' stands for Current Working Directory
print(curDir)

os.mkdir("newDir") ##'mkdir' stands for Make Directory

import time

time.sleep(2)
os.rename("newDir","newDir2")

time.sleep(2)
os.rmdir("newDir2") ##'rmdir' stands for Remove Directory

