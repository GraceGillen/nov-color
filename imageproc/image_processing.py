import pygame as pg

# grayPixel: pixel -> pixel
# compute and return a gray pixel with the same intensity
# as the given pixel
def grayPixel(pixel):
    red_intensity = pixel[0]
    green_intensity = pixel[1]
    blue_intensity = pixel[2]
    ave_intensity = (red_intensity + green_intensity+ blue_intensity)//3
    return (ave_intensity, ave_intensity, ave_intensity)

# channel: pixel -> channel -> pixel
# return a gray pixel with intensity from given channel of given pixel
def channel(pixel,chan):
    return (pixel[chan],pixel[chan],pixel[chan])


# inverse: pixel -> pixel
# return the color negative of the given pixel
def inverse(pixel):
    return (255-pixel[0], 255-pixel[1], 255-pixel[2])

def invert(image_surf):
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]
    pixels3d = pg.surfarray.pixels3d(image_surf)

    for x in range(rows):
        for y in range(cols):
            pixels3d[x,y] = inverse(pixels3d[x,y])

# intensify: pixel -> nat255 -> pixel
# brighten each channel of pixel by quantity
def intensify(pixel,quantity):
    return (pixel[0]+quantity, pixel[1]+quantity, pixel[2]+quantity)


def bw(image_surf):

    # get pixel dimensions of image
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]
    
    # get reference to and lock pixel array
    pixels3d = pg.surfarray.pixels3d(image_surf)

    # update pixels in place (side effect!)
    for x in range(rows):
        for y in range(cols):
            pixels3d[x,y] = grayPixel(pixels3d[x,y])

def lightHelp(pixel):
    if pixel[0] <= 245 and pixel[1] <= 245 and pixel[2] <= 245:
        return intensify(pixel, 10)
    else:
        return intensify(pixel, 0)
def light(image_surf):
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]
    pixels3d = pg.surfarray.pixels3d(image_surf)

    for x in range(rows):
        for y in range(cols):
            pixels3d[x,y] = lightHelp(pixels3d[x,y])


def darkHelp(pixel):
    if pixel[0] >= 10 and pixel[1] >= 10 and pixel[2] >= 10:
        return intensify(pixel, -10)
    else:
        return intensify(pixel, 0)


def dark(image_surf):
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]
    pixels3d = pg.surfarray.pixels3d(image_surf)

    for x in range(rows):
        for y in range(cols):
            pixels3d[x,y] = darkHelp(pixels3d[x,y])
