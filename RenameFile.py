import os
def rename_files():
    #get file names from a folder
    
    file_list = os.listdir(r"/Users/jantsankhorloo/Dropbox/Codes/prank")
    saved_path = os.getcwd()
    print ("Current working directory is"+saved_path)
    os.chdir(r"/Users/jantsankhorloo/Dropbox/Codes/prank")

    #for each file, rename

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789")
    os.chdir(saved_path)
    
    
#Additional useful information:
#http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
#https://docs.python.org/2/library/os.html
#http://www.tutorialspoint.com/python/string_translate.htm
