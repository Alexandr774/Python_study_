def sum_list_1(dataset: list) -> int:
    cube_list = []
    for i in range(1, 1000, 2):
        cube_list.append(i ** 3)
    summa_numbers = 0
    for i in cube_list:
        summa = 0
        m = i
        while i > 0:
            summa += i % 10
            i //= 10
        if summa % 7 == 0:
            summa_numbers += m
    return summa_numbers

my_list = []  # Соберите нужный список по заданию
result_1 = sum_list_1(my_list)
print(result_1)


def sum_list_2(dataset: list) -> int:
    cube_list = []
    for i in range(1, 1000, 2):
        cube_list.append(i ** 3 + 17)
    summa_numbers = 0
    for i in cube_list:
        summa = 0
        m = i
        while i > 0:
            summa += i % 10
            i //= 10
        if summa % 7 == 0:
            summa_numbers += m
    print(summa_numbers)


sum_list_2(my_list)
