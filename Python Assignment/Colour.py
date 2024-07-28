colour_names=["Black", "Red", "Maroon", "Yellow"]
colour_codes=["000000", "FF0000","800000", "FFFF00"]

def list_colour(names,codes):
    return[{name:code}for name,code in zip(names,codes)]


ListColour=list_colour(colour_names,colour_codes)
print(ListColour)