from uniq_name import uniq_name

def main():
    basename = uniq_name()
    photo_path = basename + ".jpg"
    thumbnail_path = basename + "s.jpg"

    print(photo_path)
    print(thumbnail_path)

if __name__ == "__main__":
    main()