def multiplication_table(n: int):
    table = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for idx_r, row in enumerate(table):
        for idx_c, col in enumerate(row):
            if (idx_r == 0) and idx_c:
                table[idx_r][idx_c] = str(idx_c)
            elif (idx_c == 0) and idx_r:
                table[idx_r][idx_c] = str(idx_r)
            else:
                table[idx_r][idx_c] = str(idx_c * idx_r)
    table[0][0] = ' '

    for row in table:
        for idx, col in enumerate(row):
            space = len([i[idx] for i in table][-1])
            print('{:>{}}'.format(col, space), end=' ')
        print()
