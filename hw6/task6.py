# бинарный поиск
# используемая парадигма функциональная, декларативная(index,filter,len)

def find_index(lst1: list, num: int):
    half = len(lst1) // 2
    left = lst1[:half]
    right = lst1[half:]

    def find_index(lst_find):
        return lst1.index(list(filter(lambda x: x == num, lst_find))[0])

    if num not in lst1:
        return -1
    if num == lst1[half]:
        return lst1.index(num)
    elif num < lst1[half]:
        return find_index(left)
    else:
        return find_index(right)


if __name__ == "__main__":
    lst = [3, 6, 7, 8, 11, 14, 23, 66, 77, 88, 99, 123,234]
    print(find_index(lst, num=990))

