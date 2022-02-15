import os
from shutil import copytree

os.chdir('my_project')
my_dir = os.getcwd()
if not os.path.isdir('templates'):
    os.mkdir('templates')

for root_dir_path, sub_dirs, files in os.walk(my_dir):
    if root_dir_path == r"C:\Users\Кирилл\PycharmProjects\helloworld\Home_Work\Dz_7\my_project\authapp\templates" or \
            root_dir_path == r'C:\Users\Кирилл\PycharmProjects\helloworld\Home_Work\Dz_7\my_project\mainapp\templates':
        copytree(root_dir_path, 'templates', dirs_exist_ok=True)
