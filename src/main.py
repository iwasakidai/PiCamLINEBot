import os
import logging
from uniq_name import uniq_name
from capture import capture_photo
from thumbnail import create_thumbnail
from upload_photo import upload_photo_to_azure
from post_photo import post_photo_via_line
from set_logging import file_handler, console_handler

# LINE投稿の撮影データのサムネイルサイズ
thumbnail_size = (240, 240)
# 撮影データの格納場所
DATA = "data/"

def main():
    # ロガーの取得
    logger = logging.getLogger(__name__)
    
    # ロガーにハンドラーを追加
    logger.addHandler(file_handler())
    logger.addHandler(console_handler())

    # ログの設定
    logger.setLevel(logging.DEBUG)

    logger.debug('データ格納フォルダ作成開始')
    # データを格納するフォルダの作成
    # なければ作成する
    if not os.path.exists(DATA):
        logger.debug('データ格納フォルダ作成')
        os.mkdir(DATA)
    logger.debug('データ格納フォルダ作成終了')

    # ユニークなファイル名の設定
    logger.debug('ユニークなファイル名の設定開始')
    basename = uniq_name()
    photo_path = "/".join(DATA, basename + ".jpg")
    thumbnail_path = "/".join(DATA, basename + "s.jpg")
    logger.debug('ユニークなファイル名の設定終了')

    # 撮影してデータを photo_path へ格納する
    logger.debug('撮影開始')
    capture_photo(photo_path)
    logger.debug('撮影終了')
    
    # サムネイル作成
    logger.debug('サムネイル作成開始')
    create_thumbnail(photo_path, thumbnail_path, size=thumbnail_size)
    logger.debug('サムネイル作成終了')

    # 撮影データ、サムネイルを Azure blob へアップロード
    logger.debug('Azure blob へアップロード開始')
    upload_photo_to_azure(photo_path)
    upload_photo_to_azure(thumbnail_path)
    logger.debug('Azure blob へアップロード終了')

    # LINE へ投稿する
    logger.debug('LINE へ投稿開始')
    post_photo_via_line(photo_path, thumbnail_path)
    logger.debug('LINE へ投稿終了')

if __name__ == "__main__":
    main()
