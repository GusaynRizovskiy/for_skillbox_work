import os
path_file = os.path.abspath(os.path.join("..","for_skillbox_work"))
def generate_function(path_file):
    for el in os.listdir(path_file):
        new_path_directory = os.path.join(path_file,el)
        sum_stroka = 0
        if os.path.isdir(new_path_directory):
            continue
        with open(new_path_directory) as cur_file:
            ch = "#"
            while True:
                line = cur_file.readline()
                if not line:
                    break
                elif  len(line)==1 or ch in line:
                    continue
                else:
                    sum_stroka+=1
        print("Количество строк в директории ",new_path_directory,)
        yield sum_stroka
id = generate_function(path_file)
for i in id:
    print(i)