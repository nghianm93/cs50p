def main():
    file_name = input("Enter the name of the file: ").strip().lower()

    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    extension = get_extension(file_name)
    media_type = media_types.get(extension, "application/octet-stream")

    print(media_type)

def get_extension(file_name):
    if "." in file_name:
        return file_name[file_name.rindex("."):]
    else:
        return ""

if __name__ == "__main__":
    main()