def key_create(round_time, key2_list56):
    key2_list28 = [] #list 28bit

    #for m in range(1, 17):
    key_time = round_time  #con thieu buoc lui 2 key cua 1 nua key1
    if ((key_time == 1) or (key_time == 2) or(key_time == 9) or (key_time == 16)):
        for m1 in range(0, 27):
            key2_list28.append(key2_list56[m1+1])
        key2_list28.append(key2_list56[0])
        for m2 in range(28, 55):
            key2_list28.append(key2_list56[m2+1])
        key2_list28.append(key2_list56[28])
    else:
        for m3 in range(0, 26):
            key2_list28.append(key2_list56[m3+2])
        key2_list28.append(key2_list56[0])
        key2_list28.append(key2_list56[1])
        for m4 in range(28, 54):
            key2_list28.append(key2_list56[m4+2])
        key2_list28.append(key2_list56[28])
        key2_list28.append(key2_list56[29])


    key_cp_table = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

    key2_list48 = [] #list 48bit after compression permutaion table

    for key_cp in range(len(key_cp_table)):
        key2_list48.append(key2_list28[key_cp_table[key_cp]-1])

    return key2_list28, key2_list48