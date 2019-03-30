X_SPACING = 16.00
Y_SPACING = 13.00
HORZ_ELEMENTS = 8
VERT_ELEMENTS = 5
Y_START = Y_SPACING * (VERT_ELEMENTS) - Y_SPACING / 2
HEADER = "# Script to arrange the diode elements on a grid of %dx%d for the audio visualizer" % (X_SPACING, Y_SPACING)

file = open("arrangeLEDS.scr", "w")

file.write(HEADER)
file.write("\n")

xpos = X_SPACING / 2.00
ypos = Y_START
diode = 1

for column in range(1, HORZ_ELEMENTS + 1):
    for row in range(1, VERT_ELEMENTS + 1):
        file.write("MOVE ")
        move = "D%d (C%f %f);\n" % (diode, xpos, ypos)
        rotate = "ROTATE =R90 'D%d';\n" % (diode)
        file.write(move)
        file.write(rotate)
        ypos -= Y_SPACING
        diode += 1
    ypos = Y_START
    xpos += X_SPACING

file.write(";")
file.close()