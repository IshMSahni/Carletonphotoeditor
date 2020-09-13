# SYSC 1005 A Fall 2018 Lab 7

import sys  # get_image calls exit
from Cimpl import *
from filters import *

def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """

    # Pop up a dialogue box to select a file

    file = choose_file()
    
    # Exit the program if the Cancel button is clicked.
    if file == "":
        sys.exit("File Open cancelled, exiting program")
    
    # Open the file containing the image and load it
    img = load_image(file)
    
    return img
# A bit of code to demonstrate how to use get_image().


if __name__ == "__main__":
    x = True
    imageloaded = False
    commands = (" L)oad \n B)lur    E)dge detect    P)osterize    S)catter    T)int sepia \n W)eighted Grayscale X)treme contrast Q)uit \n")
    
    
    while(x == True):
        answer = input(commands)
        # If answer in command tests to see if the user tries to load a filter before loading the picture and seperates all the commands so that load and quit dont run through the same if statement as the restof the filters.
        if answer in ["B", "E", "P", "S", "T", "W", "X"]:
            if imageloaded == False:
                print ("Sorry there is no image loaded")
                continue
            
            else:
                if answer == "B":  #Blur filter
                    for y in range(5): #Runs through the blur filter 5 times to make it more noticeable
                        img = blur(img)
                    show(img)
                elif answer == "E": #Edge detection better function --> also requires a threshold
                    threshold = int(input("Enter a number for for the distance of the edge of the photo: "))
                    img = detect_edges_better(img, threshold)
                    show(img)
                elif answer == "P": #Posterize function
                    img = posterize(img)
                    show(img)
                elif answer == "S": #Scatter function
                    img = scatter(img)
                    show(img)
                elif answer == "T": #Sepia Tint better function
                    img = sepia_tint(img)
                    show(img)
                elif answer == "W": #Weighted Grayscale
                    img = weighted_grayscale(img)
                    show(img) 
                elif answer == "X": #Extreme Contrast
                    img = extreme_contrast(img)
                    show(img)
                                     
                
        #This part makes sure to exit the program or load the picture more efficiently as it doesnt go through all the other code that exists
        elif answer in ["L", "Q"]:
            if answer == "L": #Load image function
                img = get_image()
                show (img)
                imageloaded = True
            elif answer == "Q":
                print ("The program will now exit.")
                x == False                           
        
        else:
            print(answer, " No such command.")
    
    
    
    
        
    
