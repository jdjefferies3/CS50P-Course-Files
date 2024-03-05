file_name = input("File name: ").strip().lower()
file_type = file_name.split(".", -1)[-1]
file_type = file_type.replace(",", "")

match file_type:
    case "gif" | "jpeg" | "png":
        print("image/", file_type, sep="")
    case "jpg":
        print("image/jpeg")
    case "pdf" | "zip":
        print("application/", file_type, sep="")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")