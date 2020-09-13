"""
SYSC 1005 Fall 2018

Filters for Lab 7. All of these filters were presented during lectures.
"""

from Cimpl import *
from random import randint

def grayscale(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
        
    return new_image


def weighted_grayscale(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a grayscale copy of the image with reference to a specific weight of each.
   
    >>> image = load_image(choose_file())
    >>> gray_image = weighted_grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = r * 0.299 + g * 0.587 + b * 0.114
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
        
    return new_image

#EXERCISE 2
def extreme_contrast(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a edited copy of image.
   
    >>> image = load_image(choose_file())
    >>> contrast_image = extreme_contrast(image)
    >>> show(contrast_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        if (0 < r < 127):
            r = 0
        else:
            r = 256;
        
        if (0 < g < 127):
            g = 0
        else:
            g = 256

        if (0 < b < 127):
            b = 0
        else:
            b = 256        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(r, g, b)
        set_color(new_image, x, y, gray)
        
    return new_image

#Exercise 3
def sepia_tint(image):
    weighted_grayscale(image)
    """ (Cimpl.Image) -> Cimpl.Image
    Returns a copy of image in which the colours have been
    converted to sepia tones.
    >>> image = load_image(choose_file())
    >>> new_image = sepia_tint(image)
    >>> show(new_image)
    """
        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.       
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
    gray = create_color(r, g, b)
    set_color(new_image, x, y, gray)   
    new_image = copy(weighted_grayscale(image))
    for x, y,(r, g, b) in new_image:
        if (r >= 62):
            set_color(new_image, x, y, create_color(r * 1.1, g, b * 0.9))
        elif (r > 62 and r < 192):
            set_color(new_image, x, y, create_color(r * 1.15, g, b * 0.85))   
        else:
            set_color(new_image, x, y, create_color(r * 1.08, g, b * 0.93))        
        
    return new_image

#EXERCISE 4
def _adjust_component(amount):
    
    """ (int) -> int

    Divide the range 0..255 into 4 equal-size quadrants,
    and return the midpoint of the quadrant in which the
    specified amount lies.

    >>> _adjust_component(10)
    31
    >>> _adjust_component(85)
    95
    >>> _adjust_component(142)
    159
    >>> _adjust_component(230)
    223
    """
    if (amount <64):
        return 31
    elif (amount >63 and amount <128):
        return 95
    elif (amount >127 and amount <192):
        return 159
    else:
        return 223
    
#EXERCISE 5
def posterize(image):
   
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a "posterized" copy of image.
  
    >>> image = load_image(choose_file())
    >>> new_image = posterize(image)
    >>> show(new_image)
    """
    new_image = copy(image)
        
        # Makes the image have a smaller number of colors than the original.      
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
    for x, y, (r, g, b) in image:
        new_color = create_color(_adjust_component(r),_adjust_component(g),_adjust_component(b))
        set_color(new_image, x, y, new_color)                
    return new_image

def blur(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a new image that is a blurred copy of image.
    
    original = load_image(choose_file())
    blurred = blur(original)
    show(blurred)    
    """  
    target = copy(image)
    
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):

            # Grab the pixel @ (x, y) and its four neighbours

            top_red, top_green, top_blue = get_color(image, x, y - 1)
            left_red, left_green, left_blue = get_color(image, x - 1, y)
            bottom_red, bottom_green, bottom_blue = get_color(image, x, y + 1)
            right_red, right_green, right_blue = get_color(image, x + 1, y)
            center_red, center_green, center_blue = get_color(image, x, y)
            
            topleft_red, topleft_green, topleft_blue = get_color (image, x - 1, y - 1)
            
            topright_red, topright_green, topright_blue = get_color(image, x + 1, y + 1)
            
            bottomleft_red, bottomleft_green, bottomleft_blue = get_color(image, x - 1, y + 1)
               
            bottomright_red, bottomright_green, bottomright_blue = get_color(image, x + 1, y + 1)            
            

            # Average the red components of the five pixels
            new_red = (top_red + left_red + bottom_red +
                       right_red + center_red +  
                       topleft_red + topright_red +  
                       bottomleft_red + bottomright_red ) // 9

            # Average the green components of the five pixels
            new_green = (top_green + left_green + bottom_green +
                                   right_green + center_green+ 
                                   topleft_green + topright_green 
                                   + bottomleft_green + bottomright_green) // 9

            # Average the blue components of the five pixels
            new_blue = (top_blue + left_blue + bottom_blue +
                                   right_blue + center_blue +
                                  topleft_blue + topright_blue + bottomleft_blue + 
                                  bottomright_blue) // 9

            new_color = create_color(new_red, new_green, new_blue)
            
            # Modify the pixel @ (x, y) in the copy of the image
            set_color(target, x, y, new_color)

    return target 

def detect_edges(image, threshold):
    new_image = copy(image)
    """ (Cimpl.Image, float) -> Cimpl.Image
    Return a new image that that is modified to black and white using edge detection.
    >>> image = load_image(choose_file())
    >>> filtered = detect_edges(image, 10.0)
    >>> show(filtered)
    """
    
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)
    
    #A loop to check all the pixels in the image
    for y in range(0, get_height(new_image) - 1):
        for x in range(0, get_width(new_image)):
            r, g, b = get_color(new_image, x, y) #Gets the rgb values of a pixel
            brightness1 = (r + g + b) / 3
            r, g, b = get_color(new_image, x, y + 1) #Gets the rgb values of a pixel near the previous
            brightness2 = (r + g + b) / 3
            if ((abs (brightness1 - brightness2)) > threshold): #if the ablsolute value of the difference of two darkened pixels is greater than the threshold then set it to black. Otherwise set it to white.
                set_color(new_image, x, y, black)
            else:
                set_color(new_image,x,y,white)
    return new_image

def detect_edges_better(image, threshold):
    new_image = copy(image)
    """ (Cimpl.Image, float) -> Cimpl.Image
    Return a new image that contains a copy of the original image
    that has been modified using edge detection.
    >>> image = load_image(choose_file())
    >>> filtered = detect_edges(image, 10.0)
    >>> show(filtered)
    """
    #The difference between this detect edges and the other is that this looks at all the pixels around the original pixel
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)
    
    for y in range(0, get_height(new_image) - 1):
        for x in range(0, get_width(new_image) - 1):
            r, g, b = get_color(new_image, x, y)
            brightness = (r + g + b) / 3
            r, g, b = get_color(new_image, x, y + 1)
            brightness_below = (r + g + b) / 3
            r, g, b = get_color(new_image, x + 1, y)
            brightness_right = (r + g + b) / 3
            calculatebelow = (abs(brightness - brightness_below)) # compares the brightness of the original pixel to the one below
            calculateright = (abs(brightness - brightness_right))
            # If either the pixel below or the one to the right is greater than the threshold, change the color of the pixel to black.
            if (calculatebelow > threshold or calculateright > threshold):
                set_color(new_image, x, y, black)
            else:
                set_color(new_image, x, y, white)
    return new_image

def grayscale(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
        
    return new_image


# The negative filter inverts every component of every pixel.
# The solarizing filter invert only those components that have intensities
# below a specified value.

def negative(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return an inverted copy of image; that is, an image that is a colour 
    negative of the original image.
    
    >>> image = load_image(choose_file())
    >>> filtered = negative(image)
    >>> show(filtered)
    """
    new_image = copy(image)
    
    # Invert the intensities of every component in every pixel.
    for  x, y, (r, g, b) in image:
        inverted = create_color(255 - r, 255 - g, 255 - b)
        set_color(new_image, x, y, inverted)

    return new_image


def solarize(image, threshold):
    """ (Cimpl.Image, int) -> Cimpl.Image
    
    Return a "solarized" copy of image. RGB components that have
    intensities less than threshold are modified.
    
    Parameter threshold is in the range 0 to 256, inclusive.
    
    >>> image = load_image(choose_file()) 
    >>> filtered = solarize(image)
    >>> show(filtered)
    """
    new_image = copy(image)
    for x, y, (red, green, blue) in image:

        # Invert the intensities of all RGB components that are less than 
        # threshold.

        if red < threshold:
            red = 255 - red

        if green < threshold:
            green = 255 - green

        if blue < threshold:
            blue = 255 - blue

        col = create_color(red, green, blue)
        set_color(new_image, x, y, col)
        
    return new_image


def black_and_white(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a black-and-white (two-tone) copy of image.
    
    >>> image = load_image(choose_file()) 
    >>> filtered = black_and_white(image)
    >>> show(filtered)
    """
    new_image = copy(image)
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255.
    # Change the colour of each pixel to black or white, depending on
    # whether its brightness is in the lower or upper half of this range.

    for x, y, (red, green, blue) in image:
        brightness = (red + green + blue) // 3
        
        if brightness < 128:  # brightness is between 0 and 127, inclusive
            set_color(new_image, x, y, black)
        else:     # brightness is between 128 and 255, inclusive
            set_color(new_image, x, y, white)
            
    return new_image


def black_and_white_and_gray(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a black-and-white-and gray (three-tone) copy of image.

    >>> image = load_image(choose_file()) 
    >>> filtered = black_and_white_and_gray(image)
    >>> show(filtered)
    """
    new_image = copy(image)
    black = create_color(0, 0, 0)
    gray = create_color(128, 128, 128)
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255. Change the colours of every
    # pixel whose brightness is in the lower third of this range to black,
    # in the upper third to white, and in the middle third to medium-gray.

    for x, y, (red, green, blue) in image:
        brightness = (red + green + blue) // 3

        if brightness < 85:    # brightness is between 0 and 84, inclusive
            set_color(new_image, x, y, black)
        elif brightness < 171: # brightness is between 85 and 170, inclusive
            set_color(new_image, x, y, gray)
        else:                  # brightness is between 171 and 255, inclusive
            set_color(new_image, x, y, white)

    return new_image

def scatter(image):
    """ (Cimpl.image) -> Cimpl.image  
    
    Return a new image that looks like a copy of an image in which the pixels
    have been randomly scattered. 
    >>> original = load_image(choose_file())
    >>> scattered = scatter(original)
    >>> show(scattered)    
    
    """
    new_image = copy(image)
    
    for x, y, (r, g, b) in new_image:
        row_and_column_are_in_bounds = False  
        while not row_and_column_are_in_bounds:
            
            randcol = randint(-10,10)
            randrow = randint(-10,10)
            random_col = x + randcol
            random_row = y + randrow      
            
            # Checks the whole picture to make sure the random column and random rows are greater than 0 but not larger than the actual picture itself. Then it sets the self explanatory variable row_and_column_are_in_bounds = True to true so then the program can proceed.
            if (random_col >= 0 and random_col <= get_width(new_image) - 1) and (random_row >= 0 and random_row <= get_height(new_image) - 1): 
                
                row_and_column_are_in_bounds = True
        newcolor = get_color(image, random_col, random_row)
        set_color(new_image, x, y, newcolor)
    return new_image

    