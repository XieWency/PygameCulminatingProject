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
quiz_complete = False
show_credits = False

main_menu_background = pygame.image.load("image folder/main_menu_background.jpg").convert()
main_menu_background = pygame.transform.scale(main_menu_background, (size))

"""
credits_page = pygame.image.load("image folder/insert... png_m").convert()
credits_page = pygame.transform.scale(credits_page, (size))
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
            def check_answer(correct_answer, user_answer):
                if user_answer == correct_answer:
                    return True
                else:
                    return False
            
            #IMPORTANT NOTES/REMINDERS: add section of code - individual question results (correct or incorrect)
                
            #declaration and initialization of variables
            state = "intro"
            keep_quiz_going = True
            exit_during_quiz = False
            correct_answers = ["C", "B", "D", "B", "A"]
            btn_multiple_choice_size = (210, 60)
                
            #font memory storage (declaration)
            choices_font = pygame.font.SysFont("comicsansms", 18)
            choices_text_colour = (102, 102, 102)
                
            #text memory storage (declaration)
            choice_a_file = ['A. 5%', 'A. verbal, nonverbal', 'A. willingness', 'A. 6 to 18 inches', 'A. sentence structure']               
            choice_b_file = ['B. 50%', 'B. nonverbal, verbal', 'B. anger', 'B. 1.5 to 4 feet', 'B. tone of voice']
            choice_c_file = ['C. 7%', 'C. not sure', 'C. disapproval', 'C. 4 to 12 feet', 'C. loudness']
            choice_d_file = ['D. 93%', 'D. none of the above', 'D. anxiety', 'D. 12 to 25 feet', 'D. pitch']
                
            #image memory storage (declaration)
            results_file = ["image folder/score_0.png", "image folder/score_1.png", "image folder/score_2.png", "image folder/score_3.png", "image folder/score_4.png", "image folder/score_5.png"]            
            questions_file = ["image folder/question_1_background.png", "image folder/question_2_background.png", "image folder/question_3_background.png", "image folder/question_4_background.png", "image folder/question_5_background.png"]
            
            intro_background_img = pygame.image.load("image folder/quiz_background.png").convert()
            intro_background_img = pygame.transform.scale(intro_background_img, size)
            correct_answers_img = pygame.image.load("image folder/correct_answers.png").convert()
            correct_answers_img = pygame.transform.scale(correct_answers_img, size)

            btn_continue_img = pygame.image.load("image folder/btn_quiz_continue.png").convert()
            btn_continue_img = pygame.transform.scale(btn_continue_img, (180, 55))
            btn_back_img = pygame.image.load("image folder/btn_quiz_back.png").convert()
            btn_back_img = pygame.transform.scale(btn_back_img, (180, 55))            
            
            btn_choice_a_img = pygame.image.load("image folder/btn_choice_img.png").convert()
            btn_choice_a_img = pygame.transform.scale(btn_choice_a_img, btn_multiple_choice_size)
            btn_choice_b_img = pygame.image.load("image folder/btn_choice_img.png").convert()
            btn_choice_b_img = pygame.transform.scale(btn_choice_b_img, btn_multiple_choice_size)
            btn_choice_c_img = pygame.image.load("image folder/btn_choice_img.png").convert()
            btn_choice_c_img = pygame.transform.scale(btn_choice_c_img, btn_multiple_choice_size)
            btn_choice_d_img = pygame.image.load("image folder/btn_choice_img.png").convert()
            btn_choice_d_img = pygame.transform.scale(btn_choice_d_img, btn_multiple_choice_size)     
                
            while keep_quiz_going and not quiz_complete:
                
                score = int(0)
                current_question = int(1)
                
                if state == "intro": #intro/instructions screen
                    screen.blit(intro_background_img, (0, 0))  
                    btn_continue = screen.blit(btn_continue_img, (630, 435)) 
                    btn_back = screen.blit(btn_back_img, (67, 435)) 
                            
                elif state == "begin": #quiz: 5 multiple choice
                    
                    while not exit_during_quiz and current_question <= 5:
                        multiple_choice_question = pygame.image.load(questions_file[current_question - 1]).convert()
                        multiple_choice_question = pygame.transform.scale(multiple_choice_question, size)
                        screen.blit(multiple_choice_question, (0, 0))  
                        
                        #coordinate variables declaration
                        pos_x_1 = 150
                        pos_x_2 = 515
                        pos_y_1 = 300
                        pos_y_2 = 400
                        border_distance = 16
                        
                        btn_choice_a = screen.blit(btn_choice_a_img, (pos_x_1, pos_y_1)) 
                        btn_choice_b = screen.blit(btn_choice_b_img, (pos_x_2, pos_y_1)) 
                        btn_choice_c = screen.blit(btn_choice_c_img, (pos_x_1, pos_y_2)) 
                        btn_choice_d = screen.blit(btn_choice_d_img, (pos_x_2, pos_y_2)) 
                        choice_a = choices_font.render((choice_a_file[current_question - 1]), True, choices_text_colour)
                        screen.blit(choice_a, (pos_x_1 + border_distance, pos_y_1 + border_distance))
                        choice_b = choices_font.render((choice_b_file[current_question - 1]), True, choices_text_colour)
                        screen.blit(choice_b, (pos_x_2 + border_distance, pos_y_1 + border_distance))
                        choice_c = choices_font.render((choice_c_file[current_question - 1]), True, choices_text_colour)
                        screen.blit(choice_c, (pos_x_1 + border_distance, pos_y_2 + border_distance))
                        choice_d = choices_font.render((choice_d_file[current_question - 1]), True, choices_text_colour)
                        screen.blit(choice_d, (pos_x_2 + border_distance, pos_y_2 + border_distance))                        
                        
                        #update and refresh the display to end this frame
                        pygame.display.flip()                        
                        
                        #handle any events in the current frame
                        for ev in pygame.event.get(): 
                                    
                            if ev.type == pygame.QUIT: #<-- this special event type happens when the window is closed
                                exit_during_quiz = True
                                keep_quiz_going = False
                                keepGoing = False
                                        
                            elif ev.type == MOUSEBUTTONDOWN:
                                pos = pygame.mouse.get_pos()  
                                if btn_choice_a.collidepoint(pos):
                                    if check_answer(correct_answers[current_question - 1], "A"):
                                        score += 1
                                    current_question += 1
                                elif btn_choice_b.collidepoint(pos):
                                    if check_answer(correct_answers[current_question - 1], "B"):
                                        score += 1    
                                    current_question += 1
                                elif btn_choice_c.collidepoint(pos):
                                    if check_answer(correct_answers[current_question - 1], "C"):
                                        score += 1
                                    current_question += 1
                                elif btn_choice_d.collidepoint(pos):
                                    if check_answer(correct_answers[current_question - 1], "D"):
                                        score += 1   
                                    current_question += 1
                        
                    if not exit_during_quiz:
                        
                        #displays answers for 3 seconds
                        screen.blit(correct_answers_img, (0, 0))  
                        pygame.display.update()   
                        pygame.time.wait(3000)      
                    
                        quiz_complete = True
                        state = "results"
                                            
                #handle any events in the current frame
                for ev in pygame.event.get(): 
                            
                    if ev.type == pygame.QUIT: #<-- this special event type happens when the window is closed
                        keep_quiz_going = False
                        keepGoing = False
                                
                    elif ev.type == MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if btn_continue.collidepoint(pos):
                            state = "begin"
                        elif btn_back.collidepoint(pos):
                            state = "main menu"
                            keep_quiz_going = False  
                            
                #update and refresh the display to end this frame
                pygame.display.flip()
                
            if quiz_complete:
                state = "results"
            
        elif state == "results":
            # ---------------code for results-------------------
            #image memory storage (declaration)            
            no_results_img = pygame.image.load("image folder/quiz_not_completed.png").convert()
            no_results_img = pygame.transform.scale(no_results_img, size)       
            
            btn_return_img = pygame.image.load("image folder/btn_quiz_return.png").convert()
            btn_return_img = pygame.transform.scale(btn_return_img, (180, 55))
            
            if quiz_complete:    
                result = pygame.image.load(results_file[score]).convert()
                result = pygame.transform.scale(result, size)   
                screen.blit(result, (0, 0))  

            else: #for backup purposes: even if the user attempts to view the results before completing the quiz, the program won't crash
                screen.blit(no_results_img, (0, 0)) 
            
            btn_return = screen.blit(btn_return_img, (67, 435))
            
            #handle any events in the current frame
            for ev in pygame.event.get(): 
                        
                if ev.type == pygame.QUIT: #<-- this special event type happens when the window is closed
                    keepGoing = False
                            
                elif ev.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if btn_return.collidepoint(pos):
                        state = "main menu"
                        
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
                    show_credits = True
                    keepGoing = False
                if btn_cont.collidepoint(pos):
                    state = "main menu"

finally:
    
    if show_credits: #excludes when window is closed
        screen.blit(credits_page, (0, 0))  
        pygame.display.flip()
        time.sleep(15)

    pygame.quit()  # keep this IDLE friendly 