def sumOfList(list):
    if len(list) == 1:
        return list[0]
    else:
        m = sumOfList(list[1:])
        return m + list[0]


if __name__ == '__main__':
    test_list = [19, 32, 25, 5, 67, 23]
    print(sumOfList(test_list))
