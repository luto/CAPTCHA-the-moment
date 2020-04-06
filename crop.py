#!/usr/bin/env python3

from datetime import datetime

from PIL import Image

import config

def find_color(im, xrange, yrange, rgbs):
    for y in range(*yrange):
        for x in range(*xrange):
            if im.getpixel((x, y)) in rgbs:
                return (x, y)

    return None

def find_color_topleft(im, rgbs):
    return find_color(im, (50,), (50,), rgbs)

def find_color_bottomright(im, rgbs):
    width, height = im.size
    return find_color(im, (width - 1, width - 50, -1), (height - 1, height - 50, -1), rgbs)

def find_box(im):
    r, g, b = im.getpixel((1, 1))

    # check if the top/left corner is ...
    #   ... white-ish, so empty backgroun
    #   ... a specific border grey
    if (r < 200 or g < 200 or b < 200) and (r, g, b) != (140, 145, 150):
        return

    # find the blue pixels of the top box ...
    first_blue = find_color_topleft(im, config.BLUE)
    # ... and the submit buttom
    last_blue = find_color_bottomright(im, config.BLUE)

    if not first_blue or not last_blue:
        return None, None
    else:
        return first_blue, last_blue


def main():
    config.CROPPED_CAPTCHA_DIR.mkdir(exist_ok=True)

    for f in config.INGESTED_CAPTCHA_DIR.glob('*.png'):
        im = Image.open(f).convert('RGB')
        top, bottom = find_box(im)
        im = im.crop((*top, *bottom))

        with open(config.CROPPED_CAPTCHA_DIR / f.name, 'wb') as ff:
            im.save(ff)


if __name__ == '__main__':
    main()
