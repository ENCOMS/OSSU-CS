# ~ $ python shirt.py
# ~ Too few command-line arguments
# ~ $ python shirt.py foo
# ~ Too few command-line arguments
# ~ $ python shirt.py foo bar
# ~ Invalid input
# ~ $ python shirt.py foo bar baz
# ~ Too many command-line arguments
# ~ $ python shirt.py before.jpg after.png
# ~ Input and output have different extensions
# ~ $ python shirt.py before.jpg after.jpg
# ~ $ python shirt.py before.png after.png

import os
import sys
from PIL import Image, ImageOps


def cmd_arg_validator():
    arg = len(sys.argv)

    match arg:
        case arg if arg <= 2:
            sys.exit("Too few command-line arguments")
        case arg if arg == 3:
            fp1, fp2 = sys.argv[1:]
            fp1, ext1 = os.path.splitext(fp1)[0], os.path.splitext(fp1)[1].lower()
            fp2, ext2 = os.path.splitext(fp2)[0], os.path.splitext(fp2)[1].lower()

            def is_valid_ext(ext):
                valid_formats = [".jpg", ".jpeg", ".png"]
                for valid_f in valid_formats:
                    if valid_f in ext:
                        return True
                return False

            valid_a = is_valid_ext(ext1)
            valid_b = is_valid_ext(ext2)

            if valid_a and valid_b == True:
                if ext1 == ext2:
                    return fp1 + ext1, fp2 + ext2
                elif ext1 != ext2:
                    sys.exit("Input and output have different extensions")
            else:
                if (valid_a == False and valid_b == True) or (
                    valid_a == False and valid_b == False
                ):
                    sys.exit("Invalid input")
                elif valid_a == True and valid_b == False:
                    sys.exit("Invalid output")
        case _:
            sys.exit("Too many command-line arguments")


def main():
    before, after = cmd_arg_validator()
    shirt = Image.open("shirt.png")
    size = shirt.size

    try:
        with Image.open(before) as image:
            photo = ImageOps.fit(image, size)
            photo.paste(shirt, shirt)
            photo.save(after)
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
