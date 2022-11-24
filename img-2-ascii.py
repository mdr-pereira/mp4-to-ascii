from PIL import Image
import sys
import numpy as np

np.set_printoptions(threshold=np.inf)

PX_SIZE = 255

GSCALE_SIMPLE = "@\#$%?*+;:\,. "
GSCALE_COMPLEX = "$@B%8&WM#*oahkbdpq/\|()1{\}[]?<>i!lI;\"^'. "

'''
Returns the average luminosity of an image, given by an array.
'''
def avg_lumin(image):
    return int(np.average(np.array(image)))

def img_2_ascii(filename, rows = 100, gscale = GSCALE_SIMPLE):
    image = Image.open(f'images/{filename}').convert('L')

    W, H = image.size

    px_per_row = int(H/rows)
    scale = W/H

    px_per_col = int(px_per_row/scale)
    cols = int(W/px_per_col)

    _img = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        y1 = int(i * px_per_row)
        y2 = y1 + px_per_row

        for j in range(cols):
            x1 = int(j * px_per_col)
            x2 = x1 + px_per_col

            crop = image.crop((x1, y1, x2, y2))

            avg = avg_lumin(crop)

            _char = gscale[int((avg * len(gscale)) / PX_SIZE) - 1]

            _img[i][j] = _char

    return _img



def main():
    #Comment
    filename = sys.argv[1]

    _img = img_2_ascii(filename, rows=500)

    with open(f"outputs/{filename.split('.')[0]}.txt", "w") as f:
        for row in _img:
            f.write("\n")
            for el in row:
                f.write(f"{el}\u2009")


if __name__ == "__main__":
    main()

