import sys
from Core import create_file,create_folder,get_list,delete_file,copy_file,save_info

save_info('Start use program')

command = sys.argv[1]

if command == 'get_list':
    get_list()

elif command == 'create_file':
    try:
        name = sys.argv[2]
        create_file(name)
        print('File' + ' ' + name + ' ' + 'created successfully!!!')
    except IndexError:
        print('Please write parameter of file')


elif command == 'create_folder':
    try:
        name = sys.argv[2]
        create_folder(name)
        print('Folder' + ' ' + name + ' ' + 'created successfully!!!')
    except IndexError:
        print('Please write parameter of folder')


elif command == 'delete':
    try:
        name = sys.argv[2]
        delete_file(name)
        print('Delete of :' + ' ' + name + ' ' + 'was made successfully!!!')
    except IndexError:
        print('Please write parameter of name')
elif command == 'copy':
    name = sys.argv[2]
    new_file = sys.argv[3]
    copy_file(name,new_file)

elif command == 'help':
    print('1) Show list of files and folders')
    print('2) Create file')
    print('3) Create folder')
    print('3) Delete file or folder')
    print('4) Copy file or folder')

save_info('Finish use program')



