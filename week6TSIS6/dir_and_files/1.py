import os

# Specify the path you want to list
path = r'C:\Users\almat\PycharmProjects\sanji'
# List only directories
print('Directories:')
for item in os.listdir(path):
    if os.path.isdir(os.path.join(path, item)):
        print(item)

# List only files
print('Files:')
for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        print(item)

# List all directories and files
print('Directories and files:')
for item in os.listdir(path):
    print(item)
