# Коэффициент корреляции пирсона


def pirson(first: list, second: list):
    def chislitel(list_1, list_2):
        temp = 0
        for itemA, itemB in zip(list_1, second):
            temp += ((itemA - sum(list_1) / len(list_1)) * (itemB - sum(list_2) / len(list_2)))
        return temp

    def func(spisok: list):
        temp = 0
        for itemA in spisok:
            temp += (itemA - sum(spisok) / len(spisok)) ** 2
        return temp
    return chislitel(first, second) / (func(first) * func(second)) ** 0.5


if __name__ == "__main__":
    one = [2, 4, 6, 8]
    two = [2, 4, 10, 12]
    print(pirson(one, two))
