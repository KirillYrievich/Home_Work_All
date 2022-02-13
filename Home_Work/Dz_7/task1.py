import os
from pathlib import Path

if not os.path.isdir('my_project'):
    os.mkdir('my_project')

os.chdir("my_project")
new_dir = Path.cwd()


def creating_folders(*names_folders):
    for i in names_folders:
        if not os.path.isdir(i):
            os.mkdir(i)


creating_folders('settings', 'mainapp', 'adminapp', 'authapp')
