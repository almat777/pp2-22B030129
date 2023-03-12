import os
path = r"C:\Users\almat\PycharmProjects\sanji\week6TSIS6\dir_and_files\ret.txt"
if os.access(path,os.F_OK):
    os.remove(path)
else:
    print("do not  exist!")