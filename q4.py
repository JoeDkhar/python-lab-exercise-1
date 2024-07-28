ListColour= ["Black", "Red", "Maroon", "Yellow"], ["000000", "FF0000",
"800000", "FFFF00"]

color_names = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["000000", "FF0000", "800000", "FFFF00"]

result = [{"colorName": name, "colorCode": code} for name, code in zip(color_names, color_codes)]
print(result)
