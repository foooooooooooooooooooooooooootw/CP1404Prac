COLOUR_CODEX = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "AQUAMARINE1": "#7fffd4", "CHOCOLATE": "#d2691e",
                "CORAL": "#ff7f50", "DARKGOLDENROD": "#b8860b", "DARKGREEN": "#006400", "DARKORCHID": "#9932cc",
                "DARKVIOLET": "#9400d3", "FIREBRICK": "#b22222"}
name_list = []
for i in COLOUR_CODEX:
    name_list.append(i)
print(name_list)

user_colour = input("Enter the colour you want the hex code for: ")

user_colour = user_colour.upper()

if user_colour not in COLOUR_CODEX:
    print("Invalid colour name.")

else:
    hex_colour = COLOUR_CODEX[user_colour]
    print("Colour code for {} is {}".format(user_colour,hex_colour))
