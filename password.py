import secrets
import string

def c_pw(pw_length=12):
    letters= string.ascii_letters
    digits = string.digits
    s_char = string.punctuation

    alph= letters+digits+s_char
    pwd=" "
    pw_strong = False

    while not pw_strong:
        pwd=" "
        for i in range(pw_length):
            pwd+= " ".join(secrets.choice(alph))

        if (any(char in s_char for char in pwd)and
             sum(char in digits for char in pwd)>=2):
            pw_strong=True

    return pwd

if __name__=='__main__':
    print(c_pw())
