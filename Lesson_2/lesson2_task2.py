el_index = int(input("Введите количество элементов списка "))
my_list = []
i = 0
el = 0
while i < el_index:
    my_list.append(input("Введите значение списка "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)
