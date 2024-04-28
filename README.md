NOTE 1 : All the examples in this page are written in Python 3.x. It may not work if you use Pyton 2.x

NOTE 2 : All the examples in this page are assumed to be written/run on Windows 7 unless specifically mentioned. You MAY (or may not) need to modify the syntax a little bit if you are running on other operating system.

Program that synchronizes two folders: source and replica After synchronization, content from replica folder should be modified to exactly match content of the source folder;

How to use: python synctask.py <source_file_path> <replica_file_path> <sync_interval> <log_file_path>

Example: python syncfiles.py \Users\username\Desktop\TestTask\Source\ \Users\username\Desktop\TestTask\Replica\ 1 \Users\username\Desktop\TestTask\FILE_OPERATIONS_LOG.txt
