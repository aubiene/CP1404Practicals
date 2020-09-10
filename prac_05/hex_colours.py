"""
Hex colours in a dictionary
"""

HEX_COLOUR_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                    "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                    "Aquamarine1": "#7fffd4", "coral": "#ff7f50", "coral3": "#cd5b45", "gray": "#bebebe"}

colour = input("Enter a colour: ")
while colour != "":
    if colour in HEX_COLOUR_CODES:
        print("{} is {}".format(colour, HEX_COLOUR_CODES[colour]))
    else:
        print("Invalid colour")
    colour_name = input("Enter a colour: ")
