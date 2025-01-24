from azure.storage.blob import BlobServiceClient
import os
import config


def upload_file_to_azure(file_path):
    """
    file_path をAzure blob へアップロードする

    Args:
        file_path (str): file のパス
    """

    try:
        # Azure Blob Storage の接続文字列
        connect_str = config.BLOB_CONNECTION_STR
        # BLOB名をファイル名そのままに
        blob_name = os.path.basename(file_path)

        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_name = "$web"
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        # ファイルを読み込む
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f"File {file_path} uploaded to Azure Blob Storage.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = "./sample.jpg"
    upload_file_to_azure(file_path)
