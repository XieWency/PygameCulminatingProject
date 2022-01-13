'''
Author Name: Wency Xie
Revision Date: January 13, 2022
Subprogram Name: Title Screen File
Description: Contains all the subprograms needed for the title screen to operate.
'''

import pygame


def display(size, screen, sub_state):
    if sub_state == "introduction":
        display_introduction(size, screen)





def display_introduction(size, screen):
    image_background(size, screen) #displays the background
    display_text(screen) #display text (name of program, student name, class code, date, and teacher name)
    image_continue_btn(screen) #displays the continue button





def handle_button_click(screen, sub_state, pos):
    if sub_state == "introduction":
        btn_cont = image_continue_btn(screen)
        if btn_cont.collidepoint(pos):
            return "main menu"
    return "title screen"





def image_background(size, screen):
    title_background = pygame.image.load("image folder/title_background.jpg")
    title_background = pygame.transform.scale(title_background, size)
    
    screen.blit(title_background, (0, 0))





def display_text(screen):
    #Declare and initialize variables
    text = str("")
    text_list = []
    normal_text_y = int(225)
    
    with open("title_screen_text.txt") as word_file:
        for word in word_file:
            text += word
    
    text_list = text.split("\n") #splits the text into an array
    
    #font
    title_font = pygame.font.SysFont("courier", 50, bold = True) #for the title
    normal_font = pygame.font.SysFont("helvetica", 17)
    
    program_name = pygame.image.load("image folder/title.png")
    program_name = pygame.transform.scale(program_name, (712, 75))
    program_name = screen.blit(program_name, (80, 100))
    
    for i in range(4):
        informational_text = normal_font.render(text_list[i], True, (0, 0, 0))
        screen.blit(informational_text, (40, normal_text_y))
        normal_text_y += 17





def image_continue_btn(screen):
    btn_cont_img = pygame.image.load("image folder/btn_continue.png")
    btn_cont_img = pygame.transform.scale(btn_cont_img, (200, 50))
    btn_cont = screen.blit(btn_cont_img, (640, 440))
    return btn_cont