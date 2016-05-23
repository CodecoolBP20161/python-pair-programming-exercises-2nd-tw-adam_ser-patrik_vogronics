a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []


def listoverlap(list1, list2):
    for element in list2:
        if element in list1:
            c.append(element)
    return c


def main():
    listoverlap(a, b)
    print(c)
    return


if __name__ == '__main__':
    main()
