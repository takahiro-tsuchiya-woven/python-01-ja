"""
# チャレンジ1

次の文字列の値があります。

- "3.14"
- "1.68"
- "9"
- "-2.5"
- "-1"

`convert.py` ファイルで次の操作を実行してください。

1. 必要に応じて `int()` または `float()` を使用して、各文字列を適切な数値に変換します。変換した各数値をそれぞれの変数に保存します。
2. これらすべての変数を合計し、結果を出力します。
"""

num1 = float("3.14")
num2 = float("1.68")
num3 = int("9")
num4 = float("-2.5")
num5 = int("-1")
#print("各数値の値は ",num1, ",", num2, ",",num3, ",",num4, ",",num5)

sum = num1 + num2 + num3 + num4 + num5
print(sum)
