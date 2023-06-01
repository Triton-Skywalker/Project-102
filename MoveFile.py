import os
import shutil

fileExtensionList = ['.txt','.doc','.docx','.pdf']
from_dir = 'C:/Users/srini/Downloads/SriRangam'
to_dir = 'C:/Users/srini/Document_FilesP102'

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    path,extension = os.path.splitext(file_name)
    
    if extension in fileExtensionList:
        path1 = from_dir + '/' + file_name
        path3 = to_dir + '/' + file_name

        if os.path.exists(to_dir):
            print('Moving ' + file_name + '....')
            shutil.move(path1,path3)
        
        else:
            os.makedirs(to_dir)
            print('Moving ' + file_name + '....')
            shutil.move(path1,path3)
    


