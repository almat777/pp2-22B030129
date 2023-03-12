import os

path = r'C:\Users\almat\PycharmProjects\sanji\week6TSIS6'
print('Directories:')
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        print(i)
print("Files")
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path, i)):
        print(i)

# List all directories and files
print('Directories and files:')
for i in os.listdir(path):
    print(i)
