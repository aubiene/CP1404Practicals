"""
Hex colours in a dictionary
"""
HEX_COLOUR_CODES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb",
                    "antiquewhite2": "#eedfcc", "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378",
                    "aquamarine1": "#7fffd4", "coral": "#ff7f50", "coral3": "#cd5b45", "gray": "#bebebe"}

colour = input("Enter a colour: ")
while colour != "":
    if colour in HEX_COLOUR_CODES:
        print("{} is {}".format(colour, HEX_COLOUR_CODES[colour]))
    else:
        print("Invalid colour")
    colour = input("Enter a colour: ")
