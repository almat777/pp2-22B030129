import os

qw = open("qwe3.txt", "r")
we = open("text.txt", "w")
for i in qw:
    we.write(str(i))
we = open("text.txt", "r")
we.read()