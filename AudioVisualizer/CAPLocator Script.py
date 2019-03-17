X_SPACING = 16.00
Y_SPACING = 13.00
HORZ_ELEMENTS = 8
VERT_ELEMENTS = 5
Y_START = Y_SPACING * (VERT_ELEMENTS) - Y_SPACING / 2  - 4.75
X_START = X_SPACING / 2.00
HEADER = "# Script to arrange the cap elements on a grid of %dx%d for the audio visualizer" % (X_SPACING, Y_SPACING)

file = open("arrangeCAPS.scr", "w")

file.write(HEADER)
file.write("\n")

xpos = X_START
ypos = Y_START
cap = 1

for column in range(1, HORZ_ELEMENTS + 1):
    for row in range(1, VERT_ELEMENTS + 1):
        file.write("MOVE ")
        move = "C%d (%f %f);\n" % (cap, xpos, ypos)
        rotate = "ROTATE =R180 'C%d';\n" % (cap)
        file.write(move)
        file.write(rotate)
        ypos -= Y_SPACING
        cap += 1
    ypos = Y_START
    xpos += X_SPACING

file.close()