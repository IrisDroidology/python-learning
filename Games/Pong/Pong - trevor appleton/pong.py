import pygame, sys # import pygame libraries into program, so we can access them. Also importing the sys libaries which are used to exit the game
from pygame.locals import *

""" Misc comments that don't fit
Line 19 - "global DISPLAYSURF" - # Creates the main surface that will be used throughout the program. Pygame draws objects onto surfaces. 
            We make the variable "global" so it can be edited/modified later throughout the program
"""

# Controlling the speed (FPS) of the program
FPS = 200 # Change this value to slow down/speed up game

# Global variables used throughout the program
# Game window
WINDOWWIDTH = 400
WINDOWHEIGHT = 300

# Writing the main function of the Pong program
def main(): # declaring the function - main function
    pygame.init() # initialising pygame
    global DISPLAYSURF # Creates the main surface that will be used throughout the program. Pygame draws objects onto surfaces
    FPSCLOCK = pygame.time.Clock() # We set the frame rate (see line 10) ourselves. This line allows the FPS to be set to that value (200) rather than the computer setting it as fast as it wants
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) # uses the values from "WINDOWHEIGHT" & "WINDOWWIDTH" - see lines 14, 15 (300px, 400px repsectively)
    pygame.display.set_caption("Stellarios/Pong by ACORD") # sets the window title/caption
    while True # Main game loop - every game needs one