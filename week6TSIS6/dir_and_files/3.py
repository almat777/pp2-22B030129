import os
path = r'C:\Users\almat\PycharmProjects\sanji\week6TSIS6\dir_and_files\ret.txt'
if os.access(path, os.F_OK):
     print(os.path.basename(path))
     print(os.path.dirname(path))
else:
     print(f"{path} do not exists")