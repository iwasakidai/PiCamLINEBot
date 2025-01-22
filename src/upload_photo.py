from azure.storage.blob import BlobServiceClient
import os
import config


def upload_photo_to_azure(photo_path):
    """
    画像データを Azure blob へアップロードする

    Args:
        photo_path (str): 撮影した画像のパス
    """

    try:
        # Azure Blob Storage の接続文字列
        connect_str = config.BLOB_CONNECTION_STR
        # BLOB名をファイル名そのままに
        blob_name = os.path.basename(photo_path)

        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_name = "$web"
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        # ファイルを読み込む
        with open(photo_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f"File {photo_path} uploaded to Azure Blob Storage.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    photo_path = "./sample.jpg"
    upload_photo_to_azure(photo_path)
