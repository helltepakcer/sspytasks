#Write a function dec_to_bin() that takes decimal integer and outputs its binary representation.

def dec_to_bin(n):
    try:
        print (bin(n))
    except:
        print("Look like you put incorrect value, please try again with other.")
        exit()

dec_to_bin("34")