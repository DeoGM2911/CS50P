from PIL import Image, ImageOps
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

# The size of the CS50 shirt is 600x600 (w.h); The size of before images are all 1200x1600
shirt = Image.open("shirt.png")
try:
    with Image.open(io_file[0]) as i_image:
        i_image = ImageOps.fit(image=i_image, size=(600, 600))
        i_image.paste(shirt, shirt)
        i_image.save(io_file[1])
except FileNotFoundError:
    sys.exit("No such file found!")
# Just in case
except OSError:
    sys.exit("Problm with input or output file!")
except ValueError:
    sys.exit("Could not determined output format!")