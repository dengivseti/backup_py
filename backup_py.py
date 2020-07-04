#!/usr/bin/env python

import os, time, pyzipper, zipfile

INPUT_FOLDER = ''
OUT_PUT = 'C:\\backup\\'
PASSWORD_ZIP = '123456'
LIST_IGNORE_FOLDER = []
LIST_IGNORE_TYPE_FILE = ['zip', 'jpg', 'png', 'jpeg']

DB_HOST = 'localhost'
DB_USER = 'root'
DB_USER_PASSWORD = ''
DB_NAME = ''
PATH_MYSQLDUMP = '"C:\\Program Files\\MySQL\\MySQL Server 5.7\\bin\\mysqldump.exe"'

TIME = time.strftime('%Y%m%d-%H%M%S')
PATH_FOLDER = OUT_PUT + TIME
print(PATH_FOLDER)
if not os.path.exists(PATH_FOLDER):
    os.mkdir(PATH_FOLDER)
FILE_SQL = TIME + ".sql"
PATH_SQL_FILE = PATH_FOLDER + "\\" + FILE_SQL

def remove_file(file):
    if os.path.exists(file):
        os.remove(file)
    else:
        print("The file does not exist")

def backup_mysql():
    try:
        if not DB_HOST or not DB_USER or not DB_USER_PASSWORD or not DB_NAME:
            print(f'Missing values')
            return
        dumpcmd = PATH_MYSQLDUMP + " -h" + DB_HOST + " -u" + DB_USER + " -p" + DB_USER_PASSWORD + " " + DB_NAME + " > " + PATH_SQL_FILE
        os.system(dumpcmd)
    except Exception as e:
        print(f'Erron {e}')

def archive():
    try:
        with zipfile.ZipFile(f'{PATH_FOLDER}\\{TIME}_old.zip', 'w', zipfile.ZIP_DEFLATED) as zip:
            for root, dirs, files in os.walk(INPUT_FOLDER):
                if os.path.basename(root) in LIST_IGNORE_FOLDER:
                    print(f'IGNORE FOLDER {os.path.basename(root)}')
                    zip.write(os.path.join(root))
                    continue
                for file in files:
                    if file.split('.')[-1] in LIST_IGNORE_TYPE_FILE:
                        continue
                    zip.write(os.path.join(root, file))
            if os.path.isfile(PATH_SQL_FILE):
                zip.write(PATH_SQL_FILE, arcname='sql\\' + FILE_SQL)
                remove_file(PATH_SQL_FILE)
        with pyzipper.AESZipFile(f'{PATH_FOLDER}\\{TIME}.zip',
                                 'w',
                                 compression=pyzipper.ZIP_LZMA,
                                 encryption=pyzipper.WZ_AES) as zf:
            zf.setpassword(PASSWORD_ZIP.encode())
            zf.write(f'{PATH_FOLDER}\\{TIME}_old.zip', arcname=f'{TIME}.zip')
            remove_file(f'{PATH_FOLDER}\\{TIME}_old.zip')
    except Exception as e:
        print(f'Erron {e}')


if __name__ == '__main__':
    backup_mysql()
    archive()
