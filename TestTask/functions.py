import os
import time
import filecmp





def is_file(name):  # function to check if its a file
    return os.path.isfile(name)

def is_folder(name):  # function to check if its a folder
    return os.path.isdir(name)

# compare files function if they are identical return TRUE 
def comparefiles(file1, file2):
    if filecmp.cmp(file1, file2, shallow=True):
        return True
    else:
        return False



# compare  folder function return True if all files are the same
def compareFolder(source, replica):
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






