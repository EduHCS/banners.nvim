import re

FILE = "ascii_arts.txt" # the file containing the ascii art banners

with open(FILE, "r") as file:
    check = re.compile(r"^ +( )  $")
    ascii_art = ""
    length = 0
    size = 0

    print("return {\n\t{\n\t\tbanner = {")

    for line in file.readlines():

        ascii_art = line.rstrip("\n")

        if re.match(check, ascii_art):
            ascii_art = ''

        if len(ascii_art) > size:
            size = len(ascii_art)

        if ascii_art[0:4] == "+---":
            print("\t\t},\n\t\tsize = " + str(size) + "\n\t},")
            print("\n\t{\n\t\tbanner = {")
            size = 0
            length += 1

        elif ascii_art != '':
            ascii_art = ascii_art.replace("\"", "\\\"")
            print('\t\t"' + ascii_art + '"')

    print("\t\t},\n\t\tsize = " + str(length) + "\n\t},")
    print("\n\tlength = " + str(length) + ",\n}")
