class Calculate_iterator():
    count = 0
    def __iter__(self):
        return self
    def __next__(self):
        Calculate_iterator.count+=1
        return  Calculate_iterator.count
id = Calculate_iterator()
for i in id:
    print(i)