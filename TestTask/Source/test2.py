
import os
import hashlib
import time
import sys
import shutil
import filecmp

source_path = sys.argv[1]
replica_path = sys.argv[2]
sync_period = sys.argv[3]
log_file_path = sys.argv[4]


#print(os.path.isabs(replica_path))
def is_file(name):  # function to check if its a file
    return os.path.isfile(name)

def is_folder(name):  # function to check if its a folder
    return os.path.isdir(name)

#print(is_folder(source_path))






def is_file(name):  # function to check if its a file
    return os.path.isfile(name)

def is_folder(name):  # function to check if its a folder
    return os.path.isdir(name)

# compare files function if they are identical return TRUE 
def comparefiles(file1, file2):
    # compare with hash
    #  'r+b' opens the file without truncation
    #with open(file1, 'rb') as f1:
       # with open(file2, 'rb') as f2:
            # hexdigest returns the hash digest as a hexadecimal string. 
            # This is a human-readable representation of the hash value. 
            # There's a very small probability of colusion.
           # if hashlib.md5(f1.read()).hexdigest() == hashlib.md5(f2.read()).hexdigest():
               # return True
           # else:
                #return False
    if filecmp.cmp(file1, file2, shallow=True):
        return True
    else:
        return False



# compare hash folder function return True if all files are the same
def compareHashFolder(source, replica):
     # get all files in replica
    files_source = os.listdir(source)
    # get all files in backup
    files_replica = os.listdir(replica)
    # compare 2 list
    if len(files_source) != len(files_replica):
        return False

    for file in files_source:
        if file in files_replica:
            if not comparefiles(source+'/'+file, replica+'/'+file):
                return False
        else:
            return False
    return True


    # get all file in source
files_source = os.listdir(source_path)
# get all file in replica
files_replica = os.listdir(replica_path)
createFile = 0 
for file in files_source:
    if is_folder(replica_path+'/'+file):
        print(file)
        if file in files_source:
            print(file)
            print(filecmp.cmp(source_path+'/'+file, replica_path+'/'+file, shallow=False))


            