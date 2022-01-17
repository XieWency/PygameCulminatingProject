'''
Author Name: Wency Xie & Sue He
Revision Date: January 17, 2022
Subprogram Name: Lesson File
Description: Contains all the subprograms needed for the lesson screen to operate.
'''

#import modules
import pygame

def display(size, screen, sub_state):
    display_background(size, screen)
    intro_button(screen)
    facial_expressions_button(screen)
    gestures_button(screen)
    posture_appearance_personal_space_button(screen)
    voice_paralinguistics_button(screen)
    main_menu_button(screen)
    
    if sub_state == "introduction":
        display_introduction(screen)
    elif sub_state == "facial expressions":
        display_facial_expressions(screen)
    elif sub_state == "gestures":
        display_gestures(screen)
    elif sub_state == "posture appearance & personal space":
        display_posture_appearance_personal_space(screen)
    elif sub_state == "voice/paralinguistics":
        display_voice_paralinguistics(screen)




def handle_button_click(screen, pos):
    btn_lesson_back = main_menu_button(screen)
    if btn_lesson_back.collidepoint(pos):
        return "main menu"
    return "lesson"




    
def handle_lesson_button_click(screen, sub_state, pos):
    btn_lesson_intro = intro_button(screen)
    btn_lesson_facial_expressions = facial_expressions_button(screen)
    btn_lesson_gestures = gestures_button(screen)
    btn_lesson_posture_appearance_personal_space = posture_appearance_personal_space_button(screen)
    btn_lesson_voice_paralinguistics = voice_paralinguistics_button(screen)
        
    if btn_lesson_intro.collidepoint(pos):
        return "introduction"
    elif btn_lesson_facial_expressions.collidepoint(pos):
        return "facial expressions"
    elif btn_lesson_gestures.collidepoint(pos):
        return "gestures"
    elif btn_lesson_posture_appearance_personal_space.collidepoint(pos):
        return "posture appearance & personal space"
    elif btn_lesson_voice_paralinguistics.collidepoint(pos):
        return "voice/paralinguistics"
    return sub_state
        





def display_background(size, screen):
    #displays the background
    screen.fill((255,255,255))
    background = pygame.image.load("image folder/lesson_background.png")
    background = pygame.transform.scale(background, size)
    
    screen.blit(background, (0, 0))





def display_introduction(screen):
    #declare and initialize variables
    text = str("")
    text_list = []
    text_y = int(120)
    
    #font
    font = pygame.font.SysFont("courier", 17, bold = True)
    
    #displays the introduction text for the lesson
    with open("text folder/introduction_text.txt") as word_file:
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





def display_facial_expressions(screen):
    #declare and initialize variables
    text = str("")
    text_list = []
    text_y = int(120)
    
    #font
    font = pygame.font.SysFont("courier", 12, bold = True)
    
    #displays the introduction text for the lesson
    with open("text folder/facial_expressions_text.txt") as word_file:
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





def display_gestures(screen):
    #declare and initialize variables
    text = str("")
    text_list = []
    text_y = int(120)
    
    #font
    font = pygame.font.SysFont("courier", 14, bold = True)
    
    #displays the introduction text for the lesson
    with open("text folder/gestures_text.txt") as word_file:
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





def display_posture_appearance_personal_space(screen):
    #declare and initialize variables
    text = str("")
    text_list = []
    text_y = int(120)
    
    #font
    font = pygame.font.SysFont("courier", 11, bold = True)
    
    #displays the introduction text for the lesson
    with open("text folder/posture_appearance_personal_space_text.txt") as word_file:
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





def display_voice_paralinguistics(screen):
    #declare and initialize variables
    text = str("")
    text_list = []
    text_y = int(120)
    
    #font
    font = pygame.font.SysFont("courier", 17, bold = True)
    
    #displays the introduction text for the lesson
    with open("text folder/voice_paralinguistics_text.txt") as word_file:
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





def intro_button(screen):
    btn_lesson_intro_img = pygame.image.load("image folder/intro_btn.png").convert()
    btn_lesson_intro = screen.blit(btn_lesson_intro_img, (25, 25))
    return btn_lesson_intro





def facial_expressions_button(screen):
    btn_lesson_facial_expressions_img = pygame.image.load("image folder/facial_expressions_btn.png").convert()
    btn_lesson_facial_expressions = screen.blit(btn_lesson_facial_expressions_img, (25, 130))
    return btn_lesson_facial_expressions





def gestures_button(screen):
    btn_lesson_gestures_img = pygame.image.load("image folder/gestures_btn.png").convert()
    btn_lesson_gestures = screen.blit(btn_lesson_gestures_img, (25, 235))
    return btn_lesson_gestures





def posture_appearance_personal_space_button(screen):
    btn_lesson_posture_appearance_personal_space_img = pygame.image.load("image folder/posture_appearance_personal_space_btn.png").convert()
    btn_lesson_posture_appearance_personal_space = screen.blit(btn_lesson_posture_appearance_personal_space_img, (25, 340))
    return btn_lesson_posture_appearance_personal_space





def voice_paralinguistics_button(screen):
    btn_lesson_voice_paralinguistics_img = pygame.image.load("image folder/voice_paralinguistics_btn.png").convert()
    btn_lesson_voice_paralinguistics = screen.blit(btn_lesson_voice_paralinguistics_img, (25, 445))
    return btn_lesson_voice_paralinguistics





def main_menu_button(screen):
    btn_lesson_back_img = pygame.image.load("image folder/lesson_back_btn.png").convert()
    btn_lesson_back = screen.blit(btn_lesson_back_img, (660, 505))
    return btn_lesson_back