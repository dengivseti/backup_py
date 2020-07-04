# backup_py
Backup folder  and mysql database in .zip archive with password.
В указанной папке будет создана дополнительная папка с текущей датой.

# VALUES

|VALUE|INFO|DAFAULT|
|----|----|----|
|INPUT_FOLDER|Folder for backup|YOU FOLDER!|
|OUT_PUT|Folder for save backup|C:\\backup\\ |
|PASSWORD_ZIP|Password .zip arhive|You password|
|LIST_IGNORE_FOLDER|Subfolders to ignore|[]|
|LIST_IGNORE_TYPE_FILE|Type file ignore|['zip', 'jpg', 'png', 'jpeg']|
|DB_HOST|Mysql host|localhost|
|DB_USER|Mysql user|root|
|DB_USER_PASSWORD|Mysql user password|You password|
|DB_NAME|You DB name for backup|''|
|PATH_MYSQLDUMP|Path for mysqldump.exe|'"C:\\Program Files\\MySQL\\MySQL Server 5.7\\bin\\mysqldump.exe"'|

# Requiments
[Zipfile](https://pypi.org/project/pyzipper/) for password .zip archive
