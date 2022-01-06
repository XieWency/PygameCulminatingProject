'''
Author Name: Wency Xie & Sue He
Revision Date: January 5, 2022
Subprogram Name: Lesson File
Description: There are different subprograms for each section of the lesson (introduction, facial expression, gestures, posture/appearance/personal space, and voice/paralinguistics).
'''

#import modules
import pygame


def display_background(size, screen):
    #displays the background
    screen.fill((255,255,255))
    background = pygame.image.load("image folder/lesson_background.png")
    background = pygame.transform.scale(background, size)
    
    screen.blit(background, (0, 0))





def display_introduction(size, screen):
    #declare and initialize variables
    text = str("")
    text_list = []
    text_y = int(120)
    
    #font
    font = pygame.font.SysFont("courier", 17, bold = True)
    
    #displays the introduction text for the lesson
    with open("introduction_text.txt") as word_file:
        for word in word_file:
            text += word
    
    text_list = text.split("\n") #splits the text into an array
    
    #displays the text
    for line in text_list:
        text_info = font.render(line, True, (0, 0, 0))
        screen.blit(text_info, (325, text_y))
        text_y += 21
    
    #displays the heading
    heading = pygame.image.load("image folder/introduction_heading.png")
    screen.blit(heading, (325, 20))





def display_facial_expressions(size, screen):
    #declare and initialize variables
    text = str("")
    text_list = []
    text_y = int(120)
    
    #font
    font = pygame.font.SysFont("courier", 12, bold = True)
    
    #displays the introduction text for the lesson
    with open("facial_expressions_text.txt") as word_file:
        for word in word_file:
            text += word
    
    text_list = text.split("\n") #splits the text into an array
    
    #displays the text
    for line in text_list:
        text_info = font.render(line, True, (0, 0, 0))
        screen.blit(text_info, (325, text_y))
        text_y += 15
    
    #displays the heading
    heading = pygame.image.load("image folder/facial_expressions_heading.png")
    screen.blit(heading, (325, 20))





def display_gestures(size, screen):
    #declare and initialize variables
    text = str("")
    text_list = []
    text_y = int(120)
    
    #font
    font = pygame.font.SysFont("courier", 14, bold = True)
    
    #displays the introduction text for the lesson
    with open("gestures_text.txt") as word_file:
        for word in word_file:
            text += word
    
    text_list = text.split("\n") #splits the text into an array
    
    #displays the text
    for line in text_list:
        text_info = font.render(line, True, (0, 0, 0))
        screen.blit(text_info, (325, text_y))
        text_y += 18
    
    #displays the heading
    heading = pygame.image.load("image folder/gestures_heading.png")
    screen.blit(heading, (325, 20))





def display_posture_appearance_personal_space(size, screen):
    #declare and initialize variables
    text = str("")
    text_list = []
    text_y = int(120)
    
    #font
    font = pygame.font.SysFont("courier", 11, bold = True)
    
    #displays the introduction text for the lesson
    with open("posture_appearance_personal_space_text.txt") as word_file:
        for word in word_file:
            text += word
    
    text_list = text.split("\n") #splits the text into an array
    
    #displays the text
    for line in text_list:
        text_info = font.render(line, True, (0, 0, 0))
        screen.blit(text_info, (325, text_y))
        text_y += 9
    
    #displays the heading
    heading = pygame.image.load("image folder/posture_appearance_personal_space_heading.png")
    screen.blit(heading, (325, 20))





def display_voice_paralinguistics(size, screen):
    #declare and initialize variables
    text = str("")
    text_list = []
    text_y = int(120)
    
    #font
    font = pygame.font.SysFont("courier", 17, bold = True)
    
    #displays the introduction text for the lesson
    with open("voice_paralinguistics_text.txt") as word_file:
        for word in word_file:
            text += word
    
    text_list = text.split("\n") #splits the text into an array
    
    #displays the text
    for line in text_list:
        text_info = font.render(line, True, (0, 0, 0))
        screen.blit(text_info, (325, text_y))
        text_y += 24
    
    #displays the heading
    heading = pygame.image.load("image folder/voice_paralinguistics_heading.png")
    screen.blit(heading, (325, 20))    