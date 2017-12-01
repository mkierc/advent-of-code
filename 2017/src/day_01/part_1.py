number_list = []

with open("data.txt") as file:
    input_data = str(file.readline())
    for character in input_data:
        number_list.append(int(character))

print(number_list)