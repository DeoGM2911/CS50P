lib_of_ext = {".gif":"image/gif",
                ".txt":"text/plain",
                ".jpeg":"image/jpeg",
                ".jpg":"image/jpeg",
                ".png":"image/png",
                ".pdf":"application/pdf",
                ".zip":"application/zip" 
            }


def main():
    fname = input("What's the file's name? \n")
    print(check_for_extension(fname))


def check_for_extension(name):
    # We can trim the code down more but for readability, I'll keep the variable extension
    extension = name[name.find('.'):]
    if extension in lib_of_ext.keys():
        return f"The type of the file is {lib_of_ext[extension]}."
    else:
        return "The type of the file is application/octet-stream."


main()