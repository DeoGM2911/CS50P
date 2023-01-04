# HTML element format
# <iframe src="URL"></iframe>
# URL can take the following forms:
# + http://youtube.com/embed/xvFZjo5PgG0
# + https://youtube.com/embed/xvFZjo5PgG0
# + https://www.youtube.com/embed/xvFZjo5PgG0
# Expected output URL: https://youtu.be/xvFZjo5PgG0

import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(html: str):
    url = re.search(r'src="(https?://(?:www\.)?youtube\.com/embed/[a-zA-Z0-9]+)"', html)
    if url is None:
        sys.exit("No URL found!")
    shorten_url = re.sub(r"https?://(www\.)?youtube\.com/embed", r"https://youtu.be", url.group(1))
    return shorten_url


if __name__ == "__main__":
    main()
