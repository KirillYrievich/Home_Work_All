import os


if not os.path.isdir('my_project'):
    os.mkdir('my_project')

os.chdir("my_project")


def creating_folders(*args):
    for i in args:
        if not os.path.isdir(i):
            os.mkdir(i)


creating_folders('settings', 'authapp', 'adminapp', 'authapp')
