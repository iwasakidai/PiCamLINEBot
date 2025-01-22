import datetime

def uniq_name() -> str:
    """
    UNIXタイムスタンプを使ったユニークな文字列を返す

    Returns:
        str: 数字16桁の文字列
    Example:
        >>> uniq_name()
        '1677192896123456_ab12cd34'
    """

    dt = datetime.datetime.now()            # ex. 2023-02-23 12:34:56.123456
    basename = str(dt.timestamp())          # ex. 1677192896.123456
    basename = basename.replace(".", "")    # ex. 1677192896123456

    return basename

if __name__ == "__main__":
    print(uniq_name())