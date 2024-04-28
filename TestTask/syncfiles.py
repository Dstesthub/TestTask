import sys
import shutil
from functions import *

source_path = sys.argv[1]
replica_path = sys.argv[2]
sync_period = sys.argv[3]
log_file_path = sys.argv[4]



# log function
def log(message):
    # write a message with local time in the last line of the LOG
    localtime = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file_path, 'a') as newline:
        newline.write('['+localtime+']'+message+'\n')




log('Start')

while True:
    # check if replica is same with source
    if compareFolder(replica_path, source_path):
        # sleep for sync_period minutes
        time.sleep(int(sync_period)*60)
        continue    

 

    # check file hash in replica and compare with source
    countcheck = 0
    createFile = 0
    copyFile = 0
    deleteFile = 0
    createFolder = 0
    copyFolder = 0
    deleteFolder = 0

    # get all file in source
    files_source = os.listdir(source_path)
    # get all file in replica
    files_replica = os.listdir(replica_path)
 
    # compare 2 list
    for file in files_replica:                    
        if file not in files_source:
            if is_file(replica_path+'/'+file):
                # delete file in replica
                log(f'{file} was removed')
                deleteFile += 1
                os.remove(replica_path+'/'+file)
            if is_folder(replica_path+'/'+file):
                # delete folder in replica
                log(f'{file} was removed')
                deleteFile += 1
                shutil.rmtree(replica_path+'/'+file)

        if is_file(replica_path+'/'+file):
            if file in files_source:
                if comparefiles(source_path+'/'+file, replica_path+'/'+file):
                    countcheck += 1
                else:
                    # copy file from source to replica
                    copyFile += 1
                    os.remove(replica_path+'/'+file)
                    shutil.copy(source_path+'/'+file, replica_path+'/'+file)
                    log(f'{file} was copied')
        if is_folder(replica_path+'/'+file):
            if file in files_source:
                if comparefiles(source_path+'/'+file, replica_path+'/'+file):
                    countcheck += 1
                else:
                    # copy folder from source to replica
                    copyFile += 1
                    shutil.rmtree(replica_path+'/'+file)
                    shutil.copytree(source_path+'/'+file, replica_path+'/'+file, dirs_exist_ok=True)
                    log(f'{file} was copied')



    for file in files_source:
        if file not in files_replica:
            if is_file(source_path+'/'+file):
                # copy file from source to replica
                createFile += 1
                log(f'{file} was created')
                shutil.copy(source_path+'/'+file, replica_path+'/'+file)
            if is_folder(source_path+'/'+file):
                # copy folder from source to replica
                createFolder += 1
                log(f'{file} was created')
                shutil.copytree(source_path+'/'+file, replica_path+'/'+file, dirs_exist_ok=False)

   


    now = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f'[{now}] Copy operation: {copyFile + copyFolder}; Creation operation: {createFile + createFolder}; Removal operation: {deleteFile + deleteFolder}; Other: {countcheck};')

    # sleep for sync_period minutes
    time.sleep(int(sync_period)*60)