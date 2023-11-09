def generator():
    with open("loging.txt","r") as file:
        file2 = open("loging2.txt","w")
        while True:
            line = file.readline()
            if not line:
                break
            else:
                if line.__contains__("Error"):
                    file2.write(line)

generator()
