import os
global_path = os.path.abspath(os.path.join("..","some_interest"))
print("Каталоги директории ",global_path)
for el in os.listdir(global_path):
    path = os.path.join(global_path,el)
    print(path)
print(global_path)