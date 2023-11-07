def genera_message(message):
    return [int(num) for num in message.rstrip().split()]

def work_chet(path_to_File):
    sum = 0
    with open(path_to_File) as my_file:
        for line in my_file:
            clear_message = sum(genera_message(line))
            yield clear_message
all_sum = 0
for number in work_chet("numbers.txt"):
    all_sum += number