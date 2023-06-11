#!bin/bash

import os 
import glob
cwd = os.getcwd() #Prints working directory
print(cwd)

ls = os.listdir()  
print(ls) #this will list your files in the directory

Dir = [] #creates empty list

filenames = glob.glob('/home/ec2-user/environment/Python1/*') #retrieve filenames

for file in filenames: #this will get your file size 
    size = os.stat(file)
    Dict = {
    file: size[6] #This makes a dictionary
    }
    Dir.append(Dict)

print(*Dir, sep='\n') #prints out the file with corresponding size