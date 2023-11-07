import os
folder_directory = "PycharmProjects"
folder_name = "success"
file_name = "admin.txt"
ot_path = os.path.join(folder_directory,folder_name,file_name)
abs_path = os.path.abspath(os.path.join("..","admin.txt"))
print(abs_path)
print(ot_path)