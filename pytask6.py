#Define a function caesar_cipher that takes string and key(number), whuch returns encrypted string


def caesar_cipher(string, key):

    alpha = "abcdefghijklmnopqrstuvwxyz"
    lenth = len(alpha)
    result = []
    for k in string:
        let_num = alpha.index(k)
        enc_word_num = let_num + (key%lenth)
        result.append(alpha[enc_word_num])
    result = "".join(result)
    print(result)

caesar_cipher("hello", 4)