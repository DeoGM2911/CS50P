import csv
from tabulate import tabulate
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line argument!")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line argument!")

# Reformat the file extension to lower case. This is for Linux which treat name case-sensitively
file = f'{sys.argv[1].split(".")[0]}.{sys.argv[1].split(".")[1].lower()}'
if not file.endswith(".csv"):
    sys.exit("No a csv file!")

try:
    with open(file, "r") as file:
        read = csv.reader(file)
        data = []
        for element in read:
            data.append(element)
    print(tabulate(data, headers="firstrow",tablefmt="grid"))

except FileNotFoundError:
    sys.exit("No such file found!")