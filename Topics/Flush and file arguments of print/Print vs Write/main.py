numbers = [1234, 5678, 90]
# save this list in `file_with_list.txt`
s_numbers = str(numbers)
with open('file_with_list.txt', 'w') as my_file:
    my_file.write(s_numbers)
