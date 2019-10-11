#!/usr/bin/python3

import sys
import random

def get_file_info(file_name):

    f = open(file_name, "r")

    contents = f.read()

    return contents

def yeet_dem_string(line, mappings):

    firstDelPos=string.find("\"")
    secondDelPos=string.find("\"")

    yeeter = gimme_a_yeet(mappings)

    stringAfterReplace = string.replace(string[firstDelPos+1:secondDelPos], yeeter)

    return line, mappings

def gimme_a_yeet(mappings):

    mappings = set(mappings.keys())

    yeet = "yeet"

    while yeet in mappings:

        random_yeet = ""

        for i in "yeet":

            a, b = random.random(), random.random()

            if a < 0.4:

                random_yeet += i

            else:

                random_yeet += i*int(a*b*10)

        yeet = ''.join(map(yeet_regular_capitalisation_away_from_me_you_piece_of_yeet, random_yeet))

    return yeet

def yeet_regular_capitalisation_away_from_me_you_piece_of_yeet(string_to_yeet):

    if random.random() > 0.5:

        return string_to_yeet.upper()

    return string_to_yeet.lower()

def yeetify(code):

    code = code.split("\n")

    mappings = {"Yeet":"return", "YEET":"main", "Yeeeet":"(", "yeeeeT":")", "yeett":"int", "yeet":"printf", "Yeeet":"{", "yeeeT":"}", "yoted":";"}

    for i in range(len(code)):

        if not "#include" in code[i] and not "#define" in code[i]:

            code[i], mappings = yeetify_line(code[i], mappings)

    for yeet, mapping in mappings.items():

        code.insert(0, "#define " + yeet + " " + mapping)

    code = "\n".join(code)

    return code

def yeetify_line(line, mappings):

    for yeet, mapping in mappings.items():

        if not mapping in "{(^:\"'!)}": mapping = " "+mapping+" "

        line = line.replace(mapping, " "+yeet+" ")

    for yeet, mapping in mappings.items():

        if not mapping in "{(^:\"'!)}": mapping = " "+mapping+" "

        line = line.replace(mapping, " "+yeet+" ")

    line = line.replace("  ", " ")

    if set(line.lower()) == {"y", "e", "t", " "}:

        return line, mappings

    return line, mappings

if __name__ == "__main__":

    file_name = sys.argv[1]

    code = get_file_info(file_name)

    print(yeetify(code))
