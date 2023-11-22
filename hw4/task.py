def pirson(first: list, second: list):
    aver_first = sum(first) / len(first)
    aver_second = sum(second) / len(second)

    def chislitel(first, second):
        temp = 0
        for itemA, itemB in zip(first, second):
            temp += ((itemA - aver_first) * (itemB - aver_second))
        return temp

    def res(spisok: list):
        temp = 0
        for itemA in spisok:
            temp += (itemA - sum(spisok) / len(spisok)) ** 2
        return temp

    return chislitel(first, second) / (res(first) * res(second)) ** 0.5


if __name__ == "__main__":
    one = [2, 4, 6, 8]
    two = [2, 4, 10, 12]
    print(pirson(one, two))
