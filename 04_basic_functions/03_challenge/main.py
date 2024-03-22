def unique_substrings(input_string):
    # 「pass」を削除して、ここにコードを書いてください
    unique_list = []
    input_string_length = len(input_string)

    for i in range(input_string_length):
        # print(i)
        for n in range(input_string_length - i):
            # print("n",n)
            # print(input_string[i: i + n + 1])
            if(input_string[i: i + n + 1] not in unique_list):
                unique_list.append(input_string[i: i + n + 1])

    return unique_list


input_string = "banana"
print(unique_substrings(input_string))
