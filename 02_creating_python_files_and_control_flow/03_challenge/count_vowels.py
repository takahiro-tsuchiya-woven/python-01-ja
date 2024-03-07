# ここにコードを書いてください
# def main():
#     # 文字列の入力
#     input_string = input('Enter a string: ')

#     # 母音のカウント
#     num_vowels = 0

#     for x in input_string:
#         if (x == 'a' or x == 'i' or x == 'u' or x == 'e' or x == 'o'):
#             num_vowels += 1

#     print('Number of vowels:' + str(num_vowels))
#     # return('Number of vowels:' + str(num_vowels))


# if  __name__ == "__main__":
#     main()


# 文字列の入力
input_string = input('Enter a string: ')

# 母音のカウント
num_vowels = 0

for x in input_string:
    if (x == 'a' or x == 'i' or x == 'u' or x == 'e' or x == 'o'):
        num_vowels += 1

print('Number of vowels:' + str(num_vowels))