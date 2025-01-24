from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    TextMessage,
    ImageMessage,
    ApiException
)
from linebot.v3.messaging.models.broadcast_request import BroadcastRequest
from pprint import pprint
import os
import config

def post_photo_via_line(photo_path, thumbnail_path):
    """
    LINE Messaging API(Broadcast)を使ってメッセージと写真を投稿する

    Args:
    photo_path (str): 写真データのパス
    thumbnail_path (str): サムネイル画像のパス

    Returns:
    None

    Note:
    This function requires the 'linebot' library to be installed.
    """
    line_access_token = config.LINE_ACCESS_TOKEN

    image_url = "https://picturesr4099f6xtfo09pyc.z11.web.core.windows.net/{}"
    if not (photo_path and thumbnail_path):
        raise FileNotFoundError("Photo or thumbnail file not found.")
    
    # 投稿する画像のURL
    photo_url = image_url.format(os.path.basename(photo_path))
    thumbnail_url = image_url.format(os.path.basename(thumbnail_path))

    # メッセージ構築
    messages = [
        TextMessage(text="写真を撮影しました！"),
        ImageMessage(
            original_content_url=photo_url,
            preview_image_url=thumbnail_url
        ),
    ]

    # Enter a context with an instance of the API client
    configuration = Configuration(access_token=line_access_token )
    with ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = MessagingApi(api_client)
        broadcast_request = BroadcastRequest(messages=messages)

        try:
            # Execute the API
            api_response = api_instance.broadcast(broadcast_request)
            print("The response of MessagingApi->broadcast:\n")
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling Api: %s\n" % e)

def main():
    photo_path = "sample.jpg"
    thumbnail_path = photo_path.replace(".jpg", "_thumbnail.jpg")
    post_photo_via_line(photo_path, thumbnail_path)

if __name__ == "__main__":
    main()
