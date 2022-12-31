import Image
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments!")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments!")

# Reformat the extension for Linux; Window and MacOS treats files by default case-insensitively and don't need this block
io_file = []
for file in sys.argv[1:]:
    io_file.append(f"{file.split('.')[0]}.{file.split('.')[1].lower()}")

if (not io_file[0].endswith(".png")) and (not io_file[0].endswith(".jpeg")) and (not io_file[0].endswith(".jpg")):
    sys.exit("Invalid input!")
elif io_file[1].split(".")[1] != io_file[0].split(".")[1]:
    sys.exit("Input and output have different extensions!")

try:
    with open(io_file[0]) as ifile:
        pass
except FileNotFoundError:
    sys.exit("No such file found!")

with open(io_file[1]) as ofile:
    pass