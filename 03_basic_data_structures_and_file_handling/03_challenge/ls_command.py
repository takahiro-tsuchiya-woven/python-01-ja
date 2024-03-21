import os


def ls_command(directory):
    # ユーザー入力が「sample」の場合、ディレクトリは「sample」になります
    # 無効なディレクトリパスについて考える必要はありません

    # 「pass」を削除して、ここにコードを書いてください
    # pass
    files = os.listdir(directory)

    result = {}

    for file in files:
        path, ext = os.path.splitext(file)

        # 拡張子がない、フォルダの場合はスキップ
        if ext == "":
            continue

        if ext in result.keys():
            result[ext] += 1
        elif ext not in result.keys():
            result[ext] = 1
    
    if any(result):
        result_sorted = sorted(result.items())
        # print(type(result_sorted))
        print("Summary in alphabetical order:")
        
        for result_sorted_print in result_sorted:
            if result_sorted_print[1] > 1:
                print(result_sorted_print[0] + ":" + str(result_sorted_print[1]) + " files")
            elif result_sorted_print[1] == 1:
                print(result_sorted_print[0] + ":" + str(result_sorted_print[1]) + " file")
    else:
        print("There is no file in the directory.")



if __name__ == "__main__":
    directory_path = input("Enter directory path to organize files: ")

    if not os.path.isdir(directory_path):
        print("Invalid directory path.")
    else:
        ls_command(directory_path)
