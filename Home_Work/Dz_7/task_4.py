import os

myDict = {}

list_100 = []
list_1000 = []
list_10000 = []
list_100000 = []

path_dir = 'some_data'

os.stat_result

stat_info = [os.stat(name).st_size for name in os.scandir(path_dir)]

for i in stat_info:
    if i <= 100:
        list_100.append(i)
    if 100 < i < 1000:
        list_1000.append(i)
    elif 1000 < i < 10000:
        list_10000.append(i)
    else:
        list_100000.append(i)

myDict[100] = len(list_100)
myDict[1000] = len(list_1000)
myDict[10000] = len(list_10000)
myDict[100000] = len(list_100000)

print(myDict)
