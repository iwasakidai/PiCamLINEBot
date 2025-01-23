import logging

def file_handler():
    """
    logging のハンドラを作成

    Args:
        None
    
    Returns:
        FileHandler class

    """
    # ハンドラーの作成
    file_handler = logging.FileHandler(filename='app.log', encoding='utf-8', mode='a')
    # フォーマッターの作成
    formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # ハンドラーにログレベルを設定
    file_handler.setLevel(logging.DEBUG)

    return file_handler

def console_handler():
    """
    logging のハンドラを作成

    Args:
        None
    
    Returns:
        StreamHandler class

    """
    # ハンドラーの作成
    console_handler = logging.StreamHandler()
    # フォーマッターの作成
    formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # ハンドラーにログレベルを設定
    console_handler.setLevel(logging.DEBUG)

    return console_handler
