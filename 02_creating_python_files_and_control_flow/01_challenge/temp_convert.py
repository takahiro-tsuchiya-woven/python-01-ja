def convert():
    # ここにコードを書いてください
    # temp変数を編集し、ユーザー入力として温度を受け取ります。整数に変換することを忘れないでください
    temp = int(input('Please enter the temperature: '))
    temp_unit = input('Please enter f for Fahrenheit or c for Celsius: ')

    if (temp_unit == 'f'):
        temp = (temp - 32) * 5/9
    elif (temp_unit == 'c'):
        temp = (temp * 9/5) + 32

    return temp


convert()
