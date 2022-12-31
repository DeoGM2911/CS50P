import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line argument!")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line argument!")
    else:
        # Reformat the file extension to lower case. This is for Linux which treat name case-sensitively
        file = f'{sys.argv[1].split(".")[0]}.{sys.argv[1].split(".")[1].lower()}'
        if not file.endswith('.py'):
            sys.exit("Not a Python file!")
        else:
            try:
                print(count_line(file))
            except FileNotFoundError:
                sys.exit("No such file found!")


def count_line(file_name: str) -> int:
        with open(file_name, "r") as pyfile:
            count = 0
            for line in pyfile:
                if (line.lstrip().startswith("#")) or (len(line.strip()) < 1):
                    continue
                count += 1
        return count


if __name__ == "__main__":
    main()
