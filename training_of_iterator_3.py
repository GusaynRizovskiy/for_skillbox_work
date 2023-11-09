import os
file2 = open("loging3.txt","w")
def error_log_generator(path):
    for line in open(path,"r"):
        if line.__contains__("Error"):
            file2.write(line)

path = os.path.abspath("loging.txt")
error_log_generator(path)