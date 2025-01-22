from PIL import Image
import os

def create_thumbnail(input_path, output_path, size=(128, 128)):
    """
    サムネイル画像を作成する関数。

    Args:
        input_path (str): 入力JPEGファイルのパス。
        output_path (str): 出力サムネイル画像のパス。
        size (tuple): サムネイルのサイズ (幅, 高さ)。
    """
    try:
        with Image.open(input_path) as img:
            img.thumbnail(size)
            img.save(output_path)
    except Exception as e:
        print(f"エラーが発生しました: {e}")

# 使用例
if __name__ == "__main__":
    input_file = "input.jpg"  # 入力画像ファイルパス
    output_file = "thumbnail.jpg"  # 出力サムネイルファイルパス
    thumbnail_size = (240, 240)  # サムネイルサイズ (LINE投稿推奨)

    if os.path.exists(input_file):
        create_thumbnail(input_file, output_file, thumbnail_size)
    else:
        print(f"入力ファイルが存在しません: {input_file}")