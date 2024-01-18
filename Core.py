import os
import shutil
import datetime


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('This is folder already exist')


# how match folders and files exists

def get_list(folders_only=False):
    result = os.listdir()  # folders_only=False
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)  # delete folder
    else:
        os.remove(name)  # delete file


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:

            shutil.copytree(name, new_name)  # copy folder
        except:
            print('This is folder already exist')
    else:
        shutil.copy(name, new_name)  # copy file


def save_info(message):  # Information of uses this program
    current_time = datetime.datetime.now()
    result = f'{current_time}-{message}'
    with open('log.txt', 'a', encoding='utf-8') as f:  # save file to f
        f.write(result + '\n')

# if __name__ == '__main__':
# create_file('text.dat', 'some text')
# create_folder('new_f')
# get_list(True)
# delete_file('text.dat')
# copy_file('new_f', 'new2')
# copy_file('text.dat', 'text2.dat')
# save_info('asdasdsad')
