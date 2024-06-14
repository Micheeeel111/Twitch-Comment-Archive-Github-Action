import os
import shutil
import subprocess

def extract_and_delete_7z(folder_path):
    """
    指定されたフォルダとそのサブフォルダ内のすべての 7z ファイルを解凍し、元の 7z ファイルを削除します。
    解凍されたファイルと削除されたファイルのリストを出力します。

    Args:
        folder_path: 解凍する 7z ファイルを含むフォルダのパス。
    """

    extracted_files = []
    deleted_files = []

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith((".7z", ".7z.*")):
                filepath = os.path.join(root, filename)

                # 7z ファイルの解凍
                try:
                    # 7z コマンドを使って解凍
                    subprocess.run(["7z", "x", filepath, "-o" + root], check=True)
                    extracted_files.append(filepath)
                except subprocess.CalledProcessError:
                    print(f"エラー: {filepath} を解凍できませんでした。")
                    continue

                # 元の 7z ファイルの削除
                os.remove(filepath)
                deleted_files.append(filepath)

    # 解凍されたファイルと削除されたファイルのリストを出力
    print("解凍されたファイル:")
    for file in extracted_files:
        print(file)

    print("\n削除されたファイル:")
    for file in deleted_files:
        print(file)

# 解凍するフォルダのリスト
folder_paths = [
    "./config",
    "./output"
]

# スクリプトの実行
for folder_path in folder_paths:
    extract_and_delete_7z(folder_path)
