import re


def main():
    print(count(input("Text: ")))


def count(s: str) -> int:
    # Add whitespace in front and behind of s to deal with the starting and ending "um".
    m = re.findall(r'\W(um)\W', ' ' + s + ' ', flags=re.IGNORECASE)
    return len(m)
    # We can change the regex to r"[^\w#$%^&*()@/\\=\-+|><{}\]\[](um+)[^\w#$%^&*()@/\\=\-+|><{}\]\[]"
    # This will delete non-logical case such as "%um" or "-um" and account for the "long" um like "ummmmm"
    # I suppose that case such as "'um'" still count with the pausing nature of the word "um".


if __name__ == "__main__":
    main()
