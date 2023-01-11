import sys
import csv

# Check for proper command-line arguments
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments!")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments!")

# Reformat the extension for Linux; Window and MacOS treats files by default case-insensitively and don't need this block
io_file = []
for file in sys.argv[1:]:
    io_file.append(f"{file.split('.')[0]}.{file.split('.')[1].lower()}")

# Check for proper command-line arguments
if not io_file[0].endswith(".csv"):
    sys.exit("Invalid input!")

# Read and reformat the data in the input file
try:
    with open(io_file[0], "r") as ifile:
        reader = csv.reader(ifile)
        data = [[], [], []]
        i = 0
        for row in reader:
            if i == 0:
                i += 1
                continue
            for id in range(2):
                data[id].append(row[0].split(",")[id].lstrip())
            data[2].append(row[1])
except FileNotFoundError:
    sys.exit(f"Could not read {io_file[0]}")

# Write the data into a new output file
with open(io_file[1], "w", newline="") as ofile:
    writer = csv.DictWriter(ofile, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for index in range(len(data[0])):
        writer.writerow({"first": data[1][index], "last": data[0][index], "house": data[2][index]})
