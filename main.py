from PIL import Image, ImageOps
import sys
from time import perf_counter
# the code can be redone to utilize gpu parallel processing

if __name__ == "__main__":
    start_perf = perf_counter()
    """
    Make a symbol table, with arbitrary amount of symbols,
    sorted from light to dark(from least filled to the most) in case of dark theme text viewer
    and vice versa in the light theme
    """
    symtable = [x for x in " .:-=+#%&@" + "_"]
    # compute the threshold(bright level) at which you'd choose one symbol over the other
    comptable = []
    comptable_step = 1 / len(symtable)
    for char in range(len(symtable)+1):
        comptable.append(char * comptable_step)
    # pop the inital zero in the compute table
    comptable.pop(0)

    def truncate(n):
        return int(n*100)/100
    # take the filename without extension, based on the dot
    filename = sys.argv[1][:sys.argv[1].find(".")]

    im = Image.open(sys.argv[1])
    im = ImageOps.grayscale(im)
    width, height = im.size[0], im.size[1]
    # for every pixel in the image, 
    # we fill a 2-dimensional matrix with the first symbol in the symtable
    ascout = [[symtable[0] for x in range(width)] for y in range(height)]
    """ 
    Iterate through each pixel in the image
    and choose an appropriate symbol from symtable,
    based on the previous compute table.
    This allows for the arbitrary amount of symbols to be used
    """
    for y in range(height):
        for x in range(width):
            curpixel = truncate(im.getpixel((x,y))/255)
            for sym in range(len(symtable)-1):
                if comptable[sym] < curpixel < comptable[sym+1]:
                    ascout[y][x] = symtable[sym]

    px_performance = perf_counter() - start_perf
    print(f"{sys.argv[1]}: finished processing {width * height} pixels in {px_performance:.3}s at {int((width * height) // px_performance)}px/s.")

    start = perf_counter()
    """
    Create a new file or overwrite an existing one with empty text
    then append every character in ascout one after the other, 
    adding a new line after each row.
    """
    with open(filename+".txt", "w") as txtout:
        txtout.write("")
    with open(filename+".txt", "a") as txtout:
        for row in ascout:
            for char in row:
                txtout.write(char)
            txtout.write("\n")
        txtout_performance = perf_counter() - start
        total_performance = px_performance + txtout_performance
        print(f"Finished writing {width * height} symbols to {filename}.txt in {txtout_performance:.3}s. Total is {total_performance:.3}s.")