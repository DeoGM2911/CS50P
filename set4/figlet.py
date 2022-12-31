# python figlet.py (ARGS here)
# if run immediately, the font will be randomly chosen
import sys
from pyfiglet import Figlet
import random as rd

fig = Figlet()
if len(sys.argv) == 1:
    text = input("Input: ")
    _font = rd.choice(fig.getFonts())
    fig.setFont(font=_font)
    print(f"Output: {fig.renderText(text)}")
elif len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in fig.getFonts():
            text = input("Input: ")
            fig.setFont(font=sys.argv[2])
            print(f"Output: {fig.renderText(text)}")
        else:
            sys.exit("No such font detected!")
    else:
        sys.exit("Invalid Argument!")
else:
    sys.exit("Invalid Argument!")
