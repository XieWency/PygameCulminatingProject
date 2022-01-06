'''
Author Name: Wency Xie
Revision Date: January 3, 2022
Subprogram Name: Title Screen
Description: Displays the title screen when called
'''

import pygame

def display_title_screen(size, screen):
    #Declare and initialize variables
    text = str("")
    text_list = []
    normal_text_y = int(250)
    
    #Display the background
    title_background = pygame.image.load("image folder/title_background.jpg")
    title_background = pygame.transform.scale(title_background, size)
    
    screen.blit(title_background, (0, 0))
    
    #Display text (name of program, student name, class code, date, and teacher name)
    with open("title_screen_text.txt") as word_file:
        for word in word_file:
            text += word
    
    text_list = text.split("\n") #splits the text into an array
    
    #fonts
    title_font = pygame.font.SysFont("courier", 50, bold = True) #for the title
    normal_font = pygame.font.SysFont("helvetica", 17) #for the other information
    
    program_name = title_font.render(text_list[0], True, (0, 50, 5)) #displaying the title
    screen.blit(program_name, (35, 110)) #I CHANGED THIS
    
    for i in range(1, 5):
        informational_text = normal_font.render(text_list[i], True, (0, 0, 0))
        screen.blit(informational_text, (40, normal_text_y))
        normal_text_y += 17