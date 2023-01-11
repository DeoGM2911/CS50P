lib_of_ext = {"gif":"image/gif",
                "txt":"text/plain",
                "jpeg":"image/jpeg",
                "jpg":"image/jpeg",
                "png":"image/png",
                "pdf":"application/pdf",
                "zip":"application/zip" 
            }


def main():
    fname = input("What's the file's name? ").strip()
    print(check_for_extension(fname), end="")


def check_for_extension(name: str):
    # We can trim the code down more but for readability, I'll keep the variable extension
    extension = name.split(".")[-1].lower()
    if extension in lib_of_ext.keys():
        return f"{lib_of_ext[extension]}"
    else:
        return "application/octet-stream"


main()