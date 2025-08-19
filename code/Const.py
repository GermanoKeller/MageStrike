# C
import pygame


C_LIGHT_YELLOW = (230, 228, 123)
C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 253, 85)

# E
ENTITY_SPEED = {
    "FireWizard": 3,
    "LMage": 3
}

# M
MENU_OPTION = ("NEW GAME 1P",
               "NEW GAME 2P",
               "SCORE",
               "EXIT")

# O
OUT_WIDTH = 1

# P
PLAYER_KEY_UP = {"FireWizard": pygame.K_w,
                 "LMage": pygame.K_UP}
PLAYER_KEY_DOWN = {"FireWizard": pygame.K_s,
                 "LMage": pygame.K_DOWN}
PLAYER_KEY_RIGHT = {"FireWizard": pygame.K_d,
                 "LMage": pygame.K_RIGHT}
PLAYER_KEY_LEFT = {"FireWizard": pygame.K_a,
                 "LMage": pygame.K_LEFT}


# W
WIN_WIDTH = 800
WIN_HEIGHT = 450