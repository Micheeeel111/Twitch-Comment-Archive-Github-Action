import os
import subprocess

def extract_and_delete_7z(folder_path):
    """
    指定されたフォルダとそのすべてのサブフォルダ内のすべての 7z マルチボリュームファイルを解凍し、
    元の 7z ファイルを削除します。解凍されたファイルと削除されたファイルのリストを出力します。

    Args:
        folder_path (str): 7z ファイルを含むフォルダのパス。
    """

    extracted_files = []
    deleted_files = []

    # フォルダを再帰的に探索
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".7z.001"):  # マルチボリュームの最初のファイルをチェック
                filepath = os.path.join(root, filename)
                print(f"処理中のファイル: {filepath}")

                # 7z ファイルの解凍 (マルチボリューム対応)
                try:
                    subprocess.run(["7z", "x", filepath, f"-o{root}"], check=True)
                    extracted_files.append(filepath)
                except subprocess.CalledProcessError as e:
                    print(f"エラー: {filepath} を解凍できませんでした。 エラーコード: {e}")
                    continue

                # すべてのボリュームファイル (.001, .002, ...) を削除
                volume_number = 1
                while True:
                    volume_file = f"{filepath[:-4]}.{str(volume_number).zfill(3)}"
                    if os.path.exists(volume_file):
                        os.remove(volume_file)
                        deleted_files.append(volume_file)
                        volume_number += 1
                    else:
                        break

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
