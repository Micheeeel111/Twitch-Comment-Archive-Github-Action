import os
import shutil
import subprocess

def compress_and_delete(folder_paths, file_size_threshold=50 * 1024 * 1024, split_size=20 * 1024 * 1024):
    """
    指定された複数のフォルダ内の特定サイズ以上のファイルを7zで圧縮し、元のファイルを削除します。
    7zの分割機能を使って、指定されたサイズで分割します。

    Args:
        folder_paths (list): 処理対象のフォルダのパスリスト
        file_size_threshold (int, optional): 圧縮対象となるファイルのサイズ閾値 (バイト単位)。デフォルトは50MB。
        split_size (int, optional): 分割するファイルサイズ (バイト単位)。デフォルトは20MB。
    """

    for folder_path in folder_paths:
        for root, _, files in os.walk(folder_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                file_size = os.path.getsize(file_path)

                if file_size >= file_size_threshold:
                    # 圧縮ファイル名を作成
                    archive_name = os.path.splitext(filename)[0] + ".7z"
                    archive_path = os.path.join(root, archive_name)

                    # 7zコマンドを実行して分割圧縮
                    subprocess.run(["7z", "a", "-t7z", "-v" + str(split_size), archive_path, file_path])

                    # 元のファイルを削除
                    os.remove(file_path)

                    print(f"{filename} を圧縮して {archive_name} に保存し、元のファイルを削除しました。")


# 処理対象のフォルダのパスリストを設定
folder_paths = [
    "./output",
    "./config",
    # ... 処理対象のフォルダを追加 ...
]

# スクリプトを実行
compress_and_delete(folder_paths)
