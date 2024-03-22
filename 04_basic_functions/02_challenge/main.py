def encode(string):
    ord_list = []
    for s in string:
        ord_list.append(str(ord(s)))

    return " ".join(ord_list)

def decode(unicode):
    str_list = []
    for u in unicode.split():
        str_list.append(chr(int(u)))
    return "".join(str_list)

print(encode("Hello World"))  # 72 101 108 108 111 32 119 111 114 108 100
print(decode("72 101 108 108 111 32 119 111 114 108 100"))  # Hello World

