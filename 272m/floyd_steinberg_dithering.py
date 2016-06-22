from PIL import Image
from sys import argv


def get_new_color_for_pixel(pixel_value):
    if isinstance(pixel_value, tuple):
        # attempt 1: if average of RGB values > 128, return 256.
        if sum(pixel_value) > 384:
            return 255, 255, 255
        else:
            return 0, 0, 0

    if pixel_value > 127:
        return 255
    else:
        return 0


def subtract_pixels(a, b):
    if isinstance(a, tuple) and isinstance(b, tuple):
        return a[0] - b[0], a[1] - b[1], a[2] - b[2]

    return a - b


def add_pixels(a, b):
    if isinstance(a, tuple) and isinstance(b, tuple):
        return a[0] + b[0], a[1] + b[1], a[2] + b[2]

    return a + b


def multiply_pixels(a, b):
    if isinstance(a, tuple):
        return int(a[0] * b), int(a[1] * b), int(a[2] * b)

    return int(a * b)


if __name__ == '__main__':
    if len(argv) < 2:
        print("Usage: %s <image filename>" % argv[0])
        exit()

    img = Image.open(argv[1])
    # 'L', (255, 255))
    pixelMap = img.load()

    width, height = img.size

    for row in range(0, height):
        for col in range(0, width):
            oldpixel = pixelMap[col, row]
            newpixel = get_new_color_for_pixel(oldpixel)
            pixelMap[col, row] = newpixel
            quant_error = subtract_pixels(oldpixel, newpixel)

            if col + 1 < width:
                pixelMap[col + 1, row] = add_pixels(pixelMap[col + 1, row], multiply_pixels(quant_error, 7 / 16))

            if row + 1 < height:
                if col - 1 >= 0:
                    pixelMap[col - 1, row + 1] = add_pixels(pixelMap[col - 1, row + 1], multiply_pixels(quant_error, 3 / 16))

                pixelMap[col, row + 1] = add_pixels(pixelMap[col, row + 1], multiply_pixels(quant_error, 5 / 16))

                if col + 1 < width:
                    pixelMap[col + 1, row + 1] = add_pixels(pixelMap[col + 1, row + 1], multiply_pixels(quant_error, 1 / 16))

    img.save("dithered_image.bmp")

    img.show()
