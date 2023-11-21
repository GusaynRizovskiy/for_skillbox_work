class File():
    def __init__(self,file_name,file_mode):
        self.file_name = file_name
        self.file_mode = file_mode
    def __enter__(self):
        self.file = open(self.file_name,self.file_mode,encoding="utf-8")
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True
with File('example.txt', 'w') as t1:
    t1.write("Всем привет")

