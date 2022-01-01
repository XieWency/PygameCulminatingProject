"""
Program Authors: Wency X. & Sue H.
Revision Date: December 24, 2021
Program Name: Python Culminating Project
Description: to be written...
"""

#import module(s)
import pygame

#pygame.locals contains constants like MOUSEMOTION and MOUSEBUTTONUP and QUIT for events
from pygame.locals import *  
#better use pygame.MOUSEMOTION

#this will allow us to name the colours to use rather than give a name eg(255,0,0)
from pygame.color import THECOLORS
#c=(255,0,0) instead of THECOLORS['red']????

#initial library itself
pygame.init()  

#just like python, we will use os and time????
import os, time

#this code is necessary for python to work on tdsb computers????
import platform
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#set-up the main screen display window and caption in the 
display_width = 880
display_height = 620
size = (display_width, display_height)  
screen = pygame.display.set_mode(size) 

#puts a caption in the bar at the top of the window
pygame.display.set_caption("to be written...") 

#sets memory screen surface with chosen background image
background_image = pygame.image.load("image folder/insert... png_x").convert()
screen.blit(background_image, (0, 0))  

#update and refresh the display to end this frame
pygame.display.flip() #<-- refresh the display

#the game loop
clock = pygame.time.Clock() #<-- used to control the frame rate
keepGoing = True 	    #<-- a 'flag' variable for the game loop condition

#set up the font and the size 
bigfont = pygame.font.SysFont("insert... font", 42)

#test=pygame.display.get_driver()
state = "title screen"

main_menu_background = pygame.image.load("image folder/insert... png_y").convert()
btn_cont = pygame.image.load("insert... gif_x").convert()
btn_animation = pygame.image.load("insert... gif_x").convert()
btn_lesson = pygame.image.load("insert... gif_y").convert()
btn_quiz = pygame.image.load("insert... gif_z").convert()
btn_results = pygame.image.load("insert... gif_a").convert()
btn_exit = pygame.image.load("insert... gif_b").convert()

animation_intro = bigfont.render(('to be written...'), True, (255,255,255))
lesson_intro = bigfont.render(('to be written...'), True, (255,255,255))
quiz_intro = bigfont.render(('to be written...'), True, (0,0,0))
no_results_comment = bigfont.render(('to be written...'), True, (200,0,10))
results_display = bigfont.render(('to be written...'), True, (200,0,10))

quiz_complete = False

try:
    while keepGoing:
        
        clock.tick(60) #delay
        screen.blit(background_image, (0, 0))  
        
        if state == "title screen":
            # -------------------button-------------------
            cont = screen.blit(btn_cont, (100, 250))            
        
        if state == "main menu":
            # ---------------code for the main menu-------------------
            screen.blit(main_menu_background, (0, 0))
            # -------------------buttons-------------------
            ba = screen.blit(btn_animation, (100, 50)) 
            bl = screen.blit(btn_lesson, (100, 100)) 
            bq = screen.blit(btn_quiz, (100, 150))
            br = screen.blit(btn_results, (100, 200))
            be = screen.blit(btn_exit, (100, 250))
   
        elif state == "animation":  
            # ---------------code for the animation-------------------               
            screen.blit(animation_intro, (20, 50))
            
        elif state == "lesson":  
            # ---------------code for the lesson-------------------               
            screen.blit(lesson_intro, (20, 50))

        elif state == "quiz":
            # ---------------code for the quiz-------------------
            screen.blit(quiz_intro, (20, 70))
            
        elif state == "results":
            # ---------------code for results-------------------
            if quiz_complete:
                screen.blit(results_display, (20, 70)) 
            else: #for backup purposes: even if the user attempts to view the results before completing the quiz, the program won't crash
                screen.blit(no_results_comment, (20, 70)) 

        pygame.display.flip()
        #handle any events in the current frame
        #print(pygame.event.get())
        
        for ev in pygame.event.get(): 
            
            if ev.type == pygame.QUIT: #<-- this special event type happens when the window is closed
                keepGoing = False
                
            elif ev.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if ba.collidepoint(pos):
                    state = "animation"
                elif bl.collidepoint(pos):
                    state = "lesson"
                elif bq.collidepoint(pos):
                    state = "quiz"      
                elif br.collidepoint(pos):
                    state = "results"                     
                elif be.collidepoint(pos):
                    keepGoing = False

finally:
    pygame.quit()  # keep this IDLE friendly 