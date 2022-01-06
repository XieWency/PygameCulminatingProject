"""
Program Authors: Wency Xie & Sue He
Revision Date: January 03, 2022
Program Name: Python Culminating Project - main file
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

#set-up the main screen display window
display_width = 880
display_height = 550
size = (display_width, display_height)  
screen = pygame.display.set_mode(size) 

#other size set-ups
main_menu_btn_size = (200, 78)

#puts a caption in the bar at the top of the window
pygame.display.set_caption("The Basics of Body Language") 

#update and refresh the display to end this frame
pygame.display.flip() #<-- refresh the display

#the game loop
clock = pygame.time.Clock() #<-- used to control the frame rate
keepGoing = True 	    #<-- a 'flag' variable for the game loop condition

#set up the font and the size 
bigfont = pygame.font.SysFont("insert... font", 42)

#test=pygame.display.get_driver()
state = "title screen"

main_menu_background = pygame.image.load("image folder/main_menu_background.png").convert()
main_menu_background = pygame.transform.scale(main_menu_background, (size))

"""
credits_background = pygame.image.load("image folder/insert... png_m").convert()
"""
btn_cont_img = pygame.image.load("image folder/btn_continue.jpg").convert()
btn_cont_img = pygame.transform.scale(btn_cont_img, (200, 50))

btn_animation_img = pygame.image.load("image folder/btn_animation.jpg").convert()
btn_animation_img = pygame.transform.scale(btn_animation_img, main_menu_btn_size)
btn_lesson_img = pygame.image.load("image folder/btn_lesson.jpg").convert()
btn_lesson_img = pygame.transform.scale(btn_lesson_img, main_menu_btn_size)
btn_quiz_img = pygame.image.load("image folder/btn_quiz.jpg").convert()
btn_quiz_img = pygame.transform.scale(btn_quiz_img, main_menu_btn_size)
btn_result_img = pygame.image.load("image folder/btn_result.jpg").convert()
btn_result_img = pygame.transform.scale(btn_result_img, main_menu_btn_size)
btn_exit_img = pygame.image.load("image folder/btn_exit.jpg").convert()
btn_exit_img = pygame.transform.scale(btn_exit_img, main_menu_btn_size)

"""
animation_intro = bigfont.render(('to be written...'), True, (255, 255, 255))
lesson_intro = bigfont.render(('to be written...'), True, (255, 255, 255))
quiz_intro = bigfont.render(('to be written...'), True, (0, 0, 0))
no_results_comment = bigfont.render(('to be written...'), True, (200, 0, 10))
results_display = bigfont.render(('to be written...'), True, (200, 0, 10))
credits_display = bigfont.render(('to be written...'), True, (0, 0, 0))
"""

quiz_complete = False

try:
    while keepGoing:
        
        clock.tick(60) #delay 
        
        if state == "title screen":
            from title_screen import display_title_screen
            display_title_screen(size, screen)
            # -------------------button-------------------
            btn_cont = screen.blit(btn_cont_img, (645, 465))            
        
        if state == "main menu":
            # ---------------code for the main menu-------------------
            screen.blit(main_menu_background, (0, 0))
            # -------------------buttons-------------------

            btn_animation = screen.blit(btn_animation_img, (600, 40)) 
            btn_lesson = screen.blit(btn_lesson_img, (600, 140)) 
            btn_quiz = screen.blit(btn_quiz_img, (600, 240))
            btn_result = screen.blit(btn_result_img, (600, 340))
            btn_exit = screen.blit(btn_exit_img, (600, 440))

   
        elif state == "animation":  
            # ---------------code for the animation-------------------               
            screen.blit(animation_intro, (20, 50))
            
        elif state == "lesson":  
            # ---------------code for the lesson-------------------               
            screen.blit(lesson_intro, (20, 50))

        elif state == "quiz":
            # ---------------code for the quiz-------------------
            from quiz import display_quiz
            display_quiz(size, screen)
            
        elif state == "results":
            # ---------------code for results-------------------
            if quiz_complete:
                import quiz
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
                if state == "main menu" and btn_animation.collidepoint(pos):
                    state = "animation"
                elif state == "main menu" and btn_lesson.collidepoint(pos):
                    state = "lesson"
                elif state == "main menu" and btn_quiz.collidepoint(pos):
                    state = "quiz"      
                elif state == "main menu" and btn_result.collidepoint(pos):
                    state = "results"                     
                elif state == "main menu" and btn_exit.collidepoint(pos):
                    keepGoing = False
                if btn_cont.collidepoint(pos):
                    state = "main menu"

finally:
    """
    screen.blit(credits_background, (0, 0))  
    screen.blit(credits_display, (20, 70))    
    time.sleep(15)
    """
    pygame.quit()  # keep this IDLE friendly 