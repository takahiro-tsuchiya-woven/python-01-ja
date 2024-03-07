def compute_factorial():
    # ここにコードを書いてください
    # number変数を編集し、ユーザー入力として正の整数を受け取ります。整数に変換することを忘れないでください
    number = int(input('Please enter an integer grater than or equal to 1: '))

    # result変数を編集し、最終的な計算結果を保存します
    result = 0

    if (number >= 0):
        result = 1
        while (number > 0):
            result = result * number
            number -= 1
    else:
        print("Please enter an integer greater than or equal to 1")

    return result


compute_factorial()
