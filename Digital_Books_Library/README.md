### セットアップと実行の手順

プロジェクトをセットアップし、実行するための具体的な手順を記述します。

## Installation and Setup

1.Clone this repository:

```　bash
git clone https://github.com/takahiro-tsuchiya-woven/python-01-ja.git
```

2.Navigate into the project directory:

``` bash
cd Digital_Books_Library
```

3.Run the project:

``` bash
python main.py
```

### プロジェクトにおける重要な設計とその設計理由

ここでは、プロジェクトの設計方針や、その設計方針を選んだ理由について説明します。

## プロジェクトの要件

[Requirements](https://app.ms1.com/learn/1BYJipoSWFWcxfxUIoruQ6/3I3QXN7QOEIZVPgW2lnoZ4/27JLohJb1gZ4l8z5tAxxKS/2ONJwNnJ1zd5mWjTBEgzRl/33TkFa4fHZGRhHAnS2HqFQ)

## プロジェクトにおける重要な設計やその設計理由

- book idの管理方法について
  - book idを追加した際に、以下のようにbook idの最終番号を保持します

  ```python
  global last_book_id
  add_book_id = last_book_id + 1
  last_book_id = add_book_id
  ```

  - これによりbook idを削除されても、最終番号から付番されていきます

### ツールまたはサービスの使い方の説明

最後に、ユーザーがプロジェクトをどのように使用するかについて説明します。具体的なコマンドや操作手順、各機能の説明などを記述します。

## 使い方

- 以下のコマンドで実行します。

```bash
python main.py
```

- 以下のメニューが表示されます。1~6を選択します。

```bash
================================================
Welcome to your personal books digital library!
================================================
1: Add a Book
2: Edit a Book
3: Search for Books
4: Delete a Book
5: View Library Stats
6: Exit app
        
Please select from 1 to 6
```

- 1: bookを追加します
  - titleとread_statusを追加します

- 2: 登録済みのbookを編集します
  - 編集するbookのIDを指定します
  - title, read_statusを変更します

- 3: 登録済みのbookを検索します
  - titleに含まれる文字列を入力します

- 4: 登録済みのbookを削除します
  - 削除するbookのIDを指定します

- 5: 統計情報および登録済みのbookを出力します

- 6: 終了します
