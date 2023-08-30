import sys
import pyfiglet
from pyfiglet import Figlet


def display_text(text, font=None):
    if font:
        fig = pyfiglet.Figlet(font=font)
    else:
        fig = pyfiglet.Figlet()

    ascii_art = fig.renderText(text)
    print(ascii_art)


def main():
    num_args = len(sys.argv)

    if num_args == 1:
        text = input("Enter the text: ")
        display_text(text)
    elif num_args == 3 and sys.argv[1] in ("-f", "--font"):
        font_name = sys.argv[2]
        figlet = Figlet()
        a = figlet.getFonts()

        if font_name in a:
            text = input("Enter the text: ")
            display_text(text, font_name)
        else:
             sys.exit(1)


    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
