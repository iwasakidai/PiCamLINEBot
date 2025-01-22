from dotenv import load_dotenv
import os

load_dotenv()

BLOB_CONNECTION_STR     = os.getenv("BLOB_CONNECTION_STR")
LINE_ACCESS_TOKEN       = os.getenv('LINE_ACCESS_TOKEN')

def main():
    print(f"BLOB_CONNECTION_STR={BLOB_CONNECTION_STR}")
    print(f"LINE_ACCESS_TOKEN={LINE_ACCESS_TOKEN }")

if __name__ == "__main__":
    main()
