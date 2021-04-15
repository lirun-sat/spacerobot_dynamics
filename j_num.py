from Get_global_value import BB
from Get_global_value import SE


def j_num(num_e):
    n = len(SE)
    j = 0
    ie = []  # list tye
    for i in range(n):
        if SE[i] == 1:
            j += 1
            ie[j] = i

    j_number = BB[ie[num_e]]
    connection = [ie[num_e]]  # connection是一个list
    while j_number != 0:
        connection.insert(0, j_number)  # 在首部插入 j_number
        j_number = BB[j_number]

    joint = connection   # return a list

    return joint



























