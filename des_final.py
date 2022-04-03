from key_final import key_create

plaintext = input("plaintext: ")
key = input("key: ")

#tao key 56bit qua permutiation lan 1
key2 = bin(int(key,16))[2:].zfill(64)
key2_list64 = list(key2)  #list key 64bit base2
key_permutation_table = [57, 49, 41, 33, 25, 17, 9,
1, 58, 50, 42, 34, 26, 18,
10, 2, 59, 51, 43, 35, 27,
19, 11, 3, 60, 52, 44, 36,
63, 55, 47, 39, 31, 23, 15,
7, 62, 54, 46, 38, 30, 22,
14, 6, 61, 53, 45, 37, 29,
21, 13, 5, 28, 20, 12, 4]

key2_list56 = []  #list 56bit after permutation table

for key_per in range(len(key_permutation_table)):
    key2_list56.append(key2_list64[key_permutation_table[key_per]-1])

#tao text 64bit ip_ermutation
text2 = bin(int(plaintext,16))[2:].zfill(64)
text2_list64 = list(text2)  #listtext 64 bits

ip_table = [58, 50, 42, 34, 26, 18, 10, 2,
60, 52, 44, 36, 28, 20, 12, 4,
62, 54, 46, 38, 30, 22, 14, 6,
64, 56, 48, 40, 32, 24, 16, 8,
57, 49, 41, 33, 25, 17, 9, 1,
59, 51, 43, 35, 27, 19, 11, 3,
61, 53, 45, 37, 29, 21, 13, 5,
63, 55, 47, 39, 31, 23, 15, 7]

text2_list64_ip = []  #list sau khi giao hoan ip

for ip in range(len(ip_table)):
    text2_list64_ip.append(text2_list64[ip_table[ip]-1])

#chia nua left, right
text2_list32_left = []
text2_list32_right = []

for half1 in range(0, 32):
    text2_list32_left.append(text2_list64_ip[half1])
for half2 in range(32, 64):
    text2_list32_right.append(text2_list64_ip[half2])

for round in range(1, 17):

    #expansion permutation table
    ep_table = [32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1]

    text2_list48_right_ep = []

    for ep_no in range(len(ep_table)):
        text2_list48_right_ep.append(text2_list32_right[ep_table[ep_no]-1])

    #cong mod2 voi khoa K
    text2_list48_right_key = []

    #goi ham khoa Key..................
    key2_list56, key2_list48 = key_create(round, key2_list56)

    for m in range(48):
        text2_list48_right_key.append((int(text2_list48_right_ep[m])+int(key2_list48[m]))%2)


    text2_cut1 = text2_list48_right_key[0:6]
    text2_cut2 = text2_list48_right_key[6:12]
    text2_cut3 = text2_list48_right_key[12:18]
    text2_cut4 = text2_list48_right_key[18:24]
    text2_cut5 = text2_list48_right_key[24:30]
    text2_cut6 = text2_list48_right_key[30:36]
    text2_cut7 = text2_list48_right_key[36:42]
    text2_cut8 = text2_list48_right_key[42:48]

    text2_list48_cut = [text2_cut1, text2_cut2, text2_cut3, text2_cut4, text2_cut5, text2_cut6, text2_cut7, text2_cut8]
    text2_list32_sbox = []

    for sbox_no in range(8):
        a = text2_list48_cut[sbox_no][0]*2 + text2_list48_cut[sbox_no][5]
        b = text2_list48_cut[sbox_no][1]*8 + text2_list48_cut[sbox_no][2]*4+text2_list48_cut[sbox_no][3]*2 + text2_list48_cut[sbox_no][4]
        s_box = []

        s1_box = [[14, 4, 13, 1, 2, 15,11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

        s2_box = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

        s3_box = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

        s4_box = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

        s5_box = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

        s6_box = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

        s7_box = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

        s8_box = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
        
        if(sbox_no == 0):
            s_box = s1_box
        elif(sbox_no == 1):
            s_box = s2_box
        elif(sbox_no == 2):
            s_box = s3_box
        elif(sbox_no == 3):
            s_box = s4_box
        elif(sbox_no == 4):
            s_box = s5_box
        elif(sbox_no == 5):
            s_box = s6_box
        elif(sbox_no == 6):
            s_box = s7_box
        elif(sbox_no == 7):
            s_box = s8_box

        c = s_box[a][b]
        c2 = str(format(c, 'b')).rjust(4,'0')
        c2_list = list(c2)
        text2_list32_sbox.extend(c2_list)

    text2_list32_pbox = []

    p_box_table = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

    for pbox_no in range(len(p_box_table)):
        text2_list32_pbox.append(text2_list32_sbox[p_box_table[pbox_no]-1])

    text2_list32_right_new = []

    for r_new in range(32):
        text2_list32_right_new.append((int(text2_list32_pbox[r_new])+int(text2_list32_left[r_new]))%2)

    text2_list32_left = text2_list32_right
    text2_list32_right = text2_list32_right_new

text2_list64_cipher = []
text2_list64_cipher.extend(text2_list32_right)
text2_list64_cipher.extend(text2_list32_left)



text2_list64_cipher_ip1 = []  #list sau khi giao hoan ip-1

ip_inverse_table = [40, 8, 48, 16, 56, 24, 64, 32,
39, 7, 47, 15, 55, 23, 63, 31,
38, 6, 46, 14, 54, 22, 62, 30,
37, 5, 45, 13, 53, 21, 61, 29,
36, 4, 44, 12, 52, 20, 60, 28,
35, 3, 43, 11, 51, 19, 59, 27,
34, 2, 42, 10, 50, 18, 58, 26,
33, 1, 41, 9, 49, 17, 57, 25]

for ip_iv in range(len(ip_inverse_table)):
    text2_list64_cipher_ip1.append(text2_list64_cipher[ip_inverse_table[ip_iv]-1])


text2_list64_cipher_ip1_str = map(str, text2_list64_cipher_ip1)

text2_cipher_10 = int(''.join(text2_list64_cipher_ip1_str),2)
text2_cipher = format(text2_cipher_10, 'x')
print(text2_cipher)