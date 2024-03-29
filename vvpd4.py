def syracuse_sequence(n):
    """
    Function to build Syracuse sequence
    :param n: Number for building sequence
    :return: list of sequence
    """
    p_list = list()
    p_list.append(n)
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            p_list.append(int(n))
        else:
            n = n * 3 + 1
            p_list.append(int(n))
    return p_list


def syracuse_max(n):
    """
    Function find to maximal elements in syracuse sequence
    :param n: number for building sequence
    :return: maximal elements in syracuse sequence
    """
    p_list = syracuse_sequence(n)
    max_n = 0
    for i in p_list:
        if i > max_n:
            max_n = i
    return max_n


print('Write Number')
number = int(input())
print('Sequence - 1 or Max - 2')
com = int(input())
if com == 1:
    print(syracuse_sequence(number))
else:
    print(syracuse_max(number))

