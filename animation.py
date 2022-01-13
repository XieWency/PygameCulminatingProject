'''
Author Name: Wency Xie & Sue He
Revision Date: January 9, 2022
Subprogram Name: Animation File
Description: Contains all the subprograms needed for the animation screen to operate.
'''

#import modules
import pygame

def display(size, screen, sub_state, sub_sub_state, choice_selected, label):
    #declare and initialize variables
    scenario_choice_size = (320, 140)
    animation_scenario_width = int(450)
    label_height = int(60)
    
    if sub_state == "instructions":                                     #display the instructions
        display_instructions(size, screen)
        continue_button(screen)
    elif sub_state == "main screen":                                            #display the main screen
        display_main_screen(size, screen)
        if sub_sub_state == "intro":
            display_intro(screen)
        elif sub_sub_state == "facial expressions":                                    #display scenario 1 (facial expressions) 
            display_scenario1(screen, animation_scenario_width, scenario_choice_size)
            if choice_selected == "A":
                display_correct_A(screen)
            elif choice_selected == "B":
                display_incorrect_B(screen)
            if choice_selected != "none":
                display_scenario1_explanation(screen, animation_scenario_width)
        elif sub_sub_state == "gestures":                                               #display scenario 2 (gestures)
            display_scenario2(screen, animation_scenario_width, scenario_choice_size)
            if choice_selected == "A":
                display_correct_A(screen)
            elif choice_selected == "B":
                display_incorrect_B(screen)
            if choice_selected != "none":
                display_scenario2_explanation(screen, animation_scenario_width)            
        elif sub_sub_state == "posture appearance & personal space":                    #display scenario 3 (posture, appearance & personal space)
            display_scenario3(screen, animation_scenario_width, scenario_choice_size)
            if choice_selected == "A":
                display_incorrect_A(screen)
            elif choice_selected == "B":
                display_correct_B(screen)
            if choice_selected != "none":
                display_scenario3_explanation(screen, animation_scenario_width)            
        elif sub_sub_state == "voice/paralinguistics":                                  #display scenario 4 (voice/paralinguistics)
            display_scenario4(screen, animation_scenario_width, scenario_choice_size)
            if choice_selected == "A":
                display_correct_A(screen)
            elif choice_selected == "B":
                display_incorrect_B(screen)
            if choice_selected != "none":
                display_scenario4_explanation(screen, animation_scenario_width)
    if label == "facial expressions":
        display_label_facial_expressions(screen, label_height)
    elif label == "gestures":
        display_label_gestures(screen, label_height)
    elif label == "posture appearance & personal space":
        display_label_posture_appearance_personal_space(screen, label_height)
    elif label == "voice/paralinguistics":
        display_label_voice_paralinguistics(screen, label_height)
    main_menu_button(screen)





def handle_button_click(screen, pos):
    btn_animation_main_menu = main_menu_button(screen)
    if btn_animation_main_menu.collidepoint(pos):
        return "main menu"
    return "animation"





def handle_animation_button_click(screen, sub_state, pos):
    if sub_state == "instructions":
        btn_animation_cont = continue_button(screen)
        if btn_animation_cont.collidepoint(pos):
            return "main screen"
    return sub_state





def handle_animation_main_screen_button_click(screen, sub_state, sub_sub_state, pos):
    if sub_state == "main screen":
        btn_animation_facial_expressions = facial_expressions_button(screen)
        btn_animation_gestures_l = gesturesl_button(screen)
        btn_animation_gestures_r = gesturesr_button(screen)
        btn_animation_posture_appearance_personal_space = posture_appearance_personal_space_button(screen)
        btn_animation_voice_paralinguistics = voice_paralinguistics_button(screen)
        
        if btn_animation_facial_expressions.collidepoint(pos):
            return "facial expressions"
        elif btn_animation_gestures_l.collidepoint(pos) or btn_animation_gestures_r.collidepoint(pos):
            return "gestures"
        elif btn_animation_posture_appearance_personal_space.collidepoint(pos):
            return "posture appearance & personal space"
        elif btn_animation_voice_paralinguistics.collidepoint(pos):
            return "voice/paralinguistics"
    return sub_sub_state





def handle_choice_selection_button_click(size, screen, sub_state, sub_sub_state, choice_selected, pos):
    scenario_choice_size = (320, 140)
    if sub_state == "main screen":
        btn_animation_facial_expressions = facial_expressions_button(screen)
        btn_animation_gestures_l = gesturesl_button(screen)
        btn_animation_gestures_r = gesturesr_button(screen)
        btn_animation_posture_appearance_personal_space = posture_appearance_personal_space_button(screen)
        btn_animation_voice_paralinguistics = voice_paralinguistics_button(screen)        
        if btn_animation_facial_expressions.collidepoint(pos) or btn_animation_gestures_l.collidepoint(pos) or btn_animation_gestures_r.collidepoint(pos) or btn_animation_posture_appearance_personal_space.collidepoint(pos) or btn_animation_voice_paralinguistics.collidepoint(pos):
            return "none"
        if sub_sub_state == "facial expressions":
            btn_animation_scenario1_choiceA = scenario1_choiceA(screen, scenario_choice_size)
            btn_animation_scenario1_choiceB = scenario1_choiceB(screen, scenario_choice_size)
            if btn_animation_scenario1_choiceA.collidepoint(pos):
                return "A"
            elif btn_animation_scenario1_choiceB.collidepoint(pos):
                return "B"
        elif sub_sub_state == "gestures":
            btn_animation_scenario2_choiceA = scenario2_choiceA(screen, scenario_choice_size)
            btn_animation_scenario2_choiceB = scenario2_choiceB(screen, scenario_choice_size) 
            if btn_animation_scenario2_choiceA.collidepoint(pos):
                return "A"
            elif btn_animation_scenario2_choiceB.collidepoint(pos):
                return "B"            
        elif sub_sub_state == "posture appearance & personal space":
            btn_animation_scenario3_choiceA = scenario3_choiceA(screen, scenario_choice_size)
            btn_animation_scenario3_choiceB = scenario3_choiceB(screen, scenario_choice_size)
            if btn_animation_scenario3_choiceA.collidepoint(pos):
                return "A"
            elif btn_animation_scenario3_choiceB.collidepoint(pos):
                return "B"            
        elif sub_sub_state == "voice/paralinguistics":
            btn_animation_scenario4_choiceA = scenario4_choiceA(screen, scenario_choice_size)
            btn_animation_scenario4_choiceB = scenario4_choiceB(screen, scenario_choice_size)
            if btn_animation_scenario4_choiceA.collidepoint(pos):
                return "A"
            elif btn_animation_scenario4_choiceB.collidepoint(pos):
                return "B"
    return choice_selected





def handle_mouse_movement(screen, sub_state, hover):
    if sub_state == "main screen":
        btn_animation_facial_expressions = facial_expressions_button(screen)
        btn_animation_gestures_l = gesturesl_button(screen)
        btn_animation_gestures_r = gesturesr_button(screen)
        btn_animation_posture_appearance_personal_space = posture_appearance_personal_space_button(screen)
        btn_animation_voice_paralinguistics = voice_paralinguistics_button(screen)
        if btn_animation_voice_paralinguistics.collidepoint(hover):
            return "voice/paralinguistics"
        elif btn_animation_facial_expressions.collidepoint(hover):
            return "facial expressions"
        elif btn_animation_gestures_l.collidepoint(hover) or btn_animation_gestures_r.collidepoint(hover):
            return "gestures"
        elif btn_animation_posture_appearance_personal_space.collidepoint(hover):
            return "posture appearance & personal space"
    return "none"





def display_main_screen(size, screen):
    display_background(size, screen)
    display_silhouette(screen)
    facial_expressions_button(screen)
    gesturesl_button(screen)
    gesturesr_button(screen)
    posture_appearance_personal_space_button(screen)
    voice_paralinguistics_button(screen)





def display_instructions(size, screen):
    instructions = pygame.image.load("image folder/animation_instructions.png").convert()
    instructions = pygame.transform.scale(instructions, (size))
    screen.blit(instructions, (0, 0))





def display_intro(screen):
    display_small_instructions(screen)





def display_scenario1(screen, x, size):
    display_scenario1_question(screen, x)
    scenario1_choiceA(screen, size)
    scenario1_choiceB(screen, size)





def display_scenario2(screen, x, size):
    display_scenario2_question(screen, x)
    scenario2_choiceA(screen, size)
    scenario2_choiceB(screen, size)





def display_scenario3(screen, x, size):
    display_scenario3_question(screen, x)
    scenario3_choiceA(screen, size)
    scenario3_choiceB(screen, size)





def display_scenario4(screen, x, size):
    display_scenario4_question(screen, x)
    scenario4_choiceA(screen, size)
    scenario4_choiceB(screen, size)





def display_background(size, screen):
    background = pygame.image.load("image folder/animation_background.jpg").convert()
    background = pygame.transform.scale(background, (size))
    screen.blit(background, (0, 0))






def display_silhouette(screen):
    silhouette = pygame.image.load("image folder/silhouette.png")
    silhouette = pygame.transform.scale(silhouette, (136, 400))
    screen.blit(silhouette, (20, 85))




#Display scenarios
def display_scenario1_question(screen, x):
    scenario = pygame.image.load("image folder/animation_scenario1.png")
    scenario = pygame.transform.scale(scenario, (x, 107))
    screen.blit(scenario, (300, 75))





def display_scenario2_question(screen, x):
    scenario = pygame.image.load("image folder/animation_scenario2.png")
    scenario = pygame.transform.scale(scenario, (x, 125))
    screen.blit(scenario, (300, 75))





def display_scenario3_question(screen, x):
    scenario = pygame.image.load("image folder/animation_scenario3.png")
    scenario = pygame.transform.scale(scenario, (x, 126))
    screen.blit(scenario, (300, 75))





def display_scenario4_question(screen, x):
    scenario = pygame.image.load("image folder/animation_scenario4.png")
    scenario = pygame.transform.scale(scenario, (x, 145))
    screen.blit(scenario, (300, 75))





#display explanations
def display_scenario1_explanation(screen, x):
    scenario = pygame.image.load("image folder/animation_scenario1_explanation.png")
    scenario = pygame.transform.scale(scenario, (x, 71))
    screen.blit(scenario, (300, 400))





def display_scenario2_explanation(screen, x):
    scenario = pygame.image.load("image folder/animation_scenario2_explanation.png")
    scenario = pygame.transform.scale(scenario, (x, 71))
    screen.blit(scenario, (300, 400))





def display_scenario3_explanation(screen, x):
    scenario = pygame.image.load("image folder/animation_scenario3_explanation.png")
    scenario = pygame.transform.scale(scenario, (x, 69))
    screen.blit(scenario, (300, 400))





def display_scenario4_explanation(screen, x):
    scenario = pygame.image.load("image folder/animation_scenario4_explanation.png")
    scenario = pygame.transform.scale(scenario, (x, 87))
    screen.blit(scenario, (300, 400))





def scenario1_choiceA(screen, size):
    btn_animation_scenario1_choiceA_img = pygame.image.load("image folder/animation_scenario1_choiceA.png")
    btn_animation_scenario1_choiceA_img = pygame.transform.scale(btn_animation_scenario1_choiceA_img, size)    
    btn_animation_scenario1_choiceA = screen.blit(btn_animation_scenario1_choiceA_img, (215, 225))
    return btn_animation_scenario1_choiceA





def scenario1_choiceB(screen, size):
    btn_animation_scenario1_choiceB_img = pygame.image.load("image folder/animation_scenario1_choiceB.png")
    btn_animation_scenario1_choiceB_img = pygame.transform.scale(btn_animation_scenario1_choiceB_img, size)    
    btn_animation_scenario1_choiceB = screen.blit(btn_animation_scenario1_choiceB_img, (550, 225))
    return btn_animation_scenario1_choiceB





def scenario2_choiceA(screen, size):
    btn_animation_scenario2_choiceA_img = pygame.image.load("image folder/animation_scenario2_choiceA.png")
    btn_animation_scenario2_choiceA_img = pygame.transform.scale(btn_animation_scenario2_choiceA_img, size)    
    btn_animation_scenario2_choiceA = screen.blit(btn_animation_scenario2_choiceA_img, (215, 225))
    return btn_animation_scenario2_choiceA





def scenario2_choiceB(screen, size):
    btn_animation_scenario2_choiceB_img = pygame.image.load("image folder/animation_scenario2_choiceB.png")
    btn_animation_scenario2_choiceB_img = pygame.transform.scale(btn_animation_scenario2_choiceB_img, size)    
    btn_animation_scenario2_choiceB = screen.blit(btn_animation_scenario2_choiceB_img, (550, 225))
    return btn_animation_scenario2_choiceB





def scenario3_choiceA(screen, size):
    btn_animation_scenario3_choiceA_img = pygame.image.load("image folder/animation_scenario3_choiceA.png")
    btn_animation_scenario3_choiceA_img = pygame.transform.scale(btn_animation_scenario3_choiceA_img, size)    
    btn_animation_scenario3_choiceA = screen.blit(btn_animation_scenario3_choiceA_img, (215, 225))
    return btn_animation_scenario3_choiceA





def scenario3_choiceB(screen, size):
    btn_animation_scenario3_choiceB_img = pygame.image.load("image folder/animation_scenario3_choiceB.png")
    btn_animation_scenario3_choiceB_img = pygame.transform.scale(btn_animation_scenario3_choiceB_img, size)    
    btn_animation_scenario3_choiceB = screen.blit(btn_animation_scenario3_choiceB_img, (550, 225))
    return btn_animation_scenario3_choiceB





def scenario4_choiceA(screen, size):
    btn_animation_scenario4_choiceA_img = pygame.image.load("image folder/animation_scenario4_choiceA.png")
    btn_animation_scenario4_choiceA_img = pygame.transform.scale(btn_animation_scenario4_choiceA_img, size)    
    btn_animation_scenario4_choiceA = screen.blit(btn_animation_scenario4_choiceA_img, (215, 225))
    return btn_animation_scenario4_choiceA





def scenario4_choiceB(screen, size):
    btn_animation_scenario4_choiceB_img = pygame.image.load("image folder/animation_scenario4_choiceB.png")
    btn_animation_scenario4_choiceB_img = pygame.transform.scale(btn_animation_scenario4_choiceB_img, size)    
    btn_animation_scenario4_choiceB = screen.blit(btn_animation_scenario4_choiceB_img, (550, 225))
    return btn_animation_scenario4_choiceB




#display labels
def display_label_facial_expressions(screen, y):
    label = pygame.image.load("image folder/animation_label_facial_expressions.png")
    label = pygame.transform.scale(label, (368, y))
    screen.blit(label, (20, 20))





def display_label_gestures(screen, y):
    label = pygame.image.load("image folder/animation_label_gestures.png")
    label = pygame.transform.scale(label, (250, y))
    screen.blit(label, (20, 20))





def display_label_posture_appearance_personal_space(screen, y):
    label = pygame.image.load("image folder/animation_label_posture_appearance_personal_space.png")
    label = pygame.transform.scale(label, (200, y))
    screen.blit(label, (20, 20))





def display_label_voice_paralinguistics(screen, y):
    label = pygame.image.load("image folder/animation_label_voice_paralinguistics.png")
    label = pygame.transform.scale(label, (310, y))
    screen.blit(label, (20, 20))





def display_small_instructions(screen):
    animation_small_instructions = pygame.image.load("image folder/animation_small_instructions.png")
    animation_small_instructions = pygame.transform.scale(animation_small_instructions, (400, 60))
    screen.blit(animation_small_instructions, (320, 245))





def display_correct_A(screen):
    check = pygame.image.load("image folder/animation_check.png")
    check = pygame.transform.scale(check, (50, 50))
    screen.blit(check, (190, 340))





def display_incorrect_A(screen):
    cross = pygame.image.load("image folder/animation_cross.png")
    cross = pygame.transform.scale(cross, (50, 50))
    screen.blit(cross, (190, 340))





def display_correct_B(screen):
    check = pygame.image.load("image folder/animation_check.png")
    check = pygame.transform.scale(check, (50, 50))
    screen.blit(check, (525, 340))





def display_incorrect_B(screen):
    cross = pygame.image.load("image folder/animation_cross.png")
    cross = pygame.transform.scale(cross, (50, 50))
    screen.blit(cross, (525, 340))





def main_menu_button(screen):
    btn_animation_main_menu_img = pygame.image.load("image folder/animation_main_menu_btn.png")
    btn_animation_main_menu_img = pygame.transform.scale(btn_animation_main_menu_img, (202, 35))
    btn_animation_main_menu = screen.blit(btn_animation_main_menu_img, (10, 505))
    return btn_animation_main_menu    





def continue_button(screen):
    btn_animation_cont_img = pygame.image.load("image folder/animation_continue_btn.png")
    btn_animation_cont_img = pygame.transform.scale(btn_animation_cont_img, (172, 35))
    btn_animation_cont = screen.blit(btn_animation_cont_img, (698, 505))
    return btn_animation_cont    





def facial_expressions_button(screen):
    btn_animation_facial_expressions_img = pygame.image.load("image folder/silhouette_facial_expressions.png")
    btn_animation_facial_expressions_img = pygame.transform.scale(btn_animation_facial_expressions_img, (39, 47))
    btn_animation_facial_expressions = screen.blit(btn_animation_facial_expressions_img, (68, 85))
    return btn_animation_facial_expressions    





def gesturesl_button(screen):
    btn_animation_gestures_l_img = pygame.image.load("image folder/silhouette_gestures_left.png")
    btn_animation_gestures_l_img = pygame.transform.scale(btn_animation_gestures_l_img, (19, 45))
    btn_animation_gestures_l = screen.blit(btn_animation_gestures_l_img, (20, 280))
    return btn_animation_gestures_l  





def gesturesr_button(screen):
    btn_animation_gestures_r_img = pygame.image.load("image folder/silhouette_gestures_right.png")
    btn_animation_gestures_r_img = pygame.transform.scale(btn_animation_gestures_r_img, (19, 45))
    btn_animation_gestures_r = screen.blit(btn_animation_gestures_r_img, (138, 280))
    return btn_animation_gestures_r  





def posture_appearance_personal_space_button(screen):
    btn_animation_posture_appearance_personal_space_img = pygame.image.load("image folder/silhouette_posture_appearance_personal_space.png")
    btn_animation_posture_appearance_personal_space_img = pygame.transform.scale(btn_animation_posture_appearance_personal_space_img, (113, 104))
    btn_animation_posture_appearance_personal_space = screen.blit(btn_animation_posture_appearance_personal_space_img, (32, 150))
    return btn_animation_posture_appearance_personal_space  





def voice_paralinguistics_button(screen):
    btn_animation_voice_paralinguistics_img = pygame.image.load("image folder/silhouette_voice_paralinguistics.png")
    btn_animation_voice_paralinguistics_img = pygame.transform.scale(btn_animation_voice_paralinguistics_img, (87, 21))
    btn_animation_voice_paralinguistics = screen.blit(btn_animation_voice_paralinguistics_img, (43, 131))
    return btn_animation_voice_paralinguistics  