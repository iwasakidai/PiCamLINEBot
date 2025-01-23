from uniq_name import uniq_name
from capture import capture_photo
from thumbnail import create_thumbnail
from upload_photo import upload_photo_to_azure
from post_photo import post_photo_via_line

# LINE投稿の撮影データのサムネイルサイズ
thumbnail_size = (240, 240)

def main():
    # ユニークなファイル名の設定
    basename = uniq_name()
    photo_path = basename + ".jpg"
    thumbnail_path = basename + "s.jpg"

    # 撮影してデータを photo_path へ格納する
    capture_photo(photo_path)
    
    # サムネイル作成
    create_thumbnail(photo_path, thumbnail_path, size=thumbnail_size)

    # 撮影データ、サムネイルを Azure blob へアップロード
    upload_photo_to_azure(photo_path)
    upload_photo_to_azure(thumbnail_path)

    # LINE へ投稿する
    post_photo_via_line(photo_path, thumbnail_path)

if __name__ == "__main__":
    main()
