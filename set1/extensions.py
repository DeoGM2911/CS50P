def check_for_extension():
    while True:
        fname = input("What's the file's name? \n")
        if fname == '1': break
        pos_extension = fname.find('.')
        extension = fname[pos_extension:]
        lib_of_ext = {".gif":"image/gif",
                    ".txt":"text/plain",
                    ".jpeg":"image/jpeg",
                    ".jpg":"image/jpeg",
                    ".png":"image/png",
                    ".pdf":"application/pdf",
                    ".zip":"application/zip" 
                    }
        if extension in lib_of_ext.keys():
            print(f"The type of the file is {lib_of_ext[extension]}.")
        else:
            print("The type of the file is application/octet-stream.")
check_for_extension()