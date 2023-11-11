# написать код сортировки  списка по убыванию в императивном и декларативном стиле

def sort_list_impertive(numbers):
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] <= numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


def sort_list_declarative(numbers: list):
    numbers.sort(reverse=True)
    return numbers


if __name__ == "__main__":
    num = [5, 6, 8, 23, 4, 1, 0, 3]
    print(sort_list_impertive(num))
    print(sort_list_declarative(num))
