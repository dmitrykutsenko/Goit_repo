#function that will unpack the archive using the shutil module. Here is one possible solution:

def unpack(archive_path, path_to_unpack):

    #Use the shutil.unpack_archive method to unpack the archive
    shutil.unpack_archive(archive_path, path_to_unpack)

#The function does not return anything
#This function will call the shutil.unpack_archive method and unpack the archive_path archive into the path_to_unpack location. It will not return anything. However, it will not handle any errors or exceptions that may occur while unpacking the archive