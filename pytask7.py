#define a function diaginal_reverse() that takes matrix and returns diagonal-reversed one:

#1 2 3         1 4 7
#4 5 6 returns 2 5 8
#7 8 9         3 6 9


def digital_reverse(n):
    dig_mat = [[],[],[]]
    k = 0
    for num in range(0, len(n)):
        for sonew in n:
            dig_mat[num].append(sonew[num])
            print(dig_mat)
    return dig_mat


digital_reverse([[1,2,3],[4,5,6],[7,8,9]])


