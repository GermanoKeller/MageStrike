# C
import pygame


C_LIGHT_YELLOW = (230, 228, 123)
C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 253, 85)

# E
ENTITY_SPEED = {
    "FWizard": 3,
    "FWizardShot": 3,
    "LMage": 3,
    "LMageShot": 3,
    "Enemy": 1.5,
    "EnemyShot": 3
}

ENTITY_HEALTH = {
    "Level1Bg0": 999,
    "Level1Bg1": 999,
    "Level1Bg2": 999,
    "Level1Bg3": 999,
    "Level1Bg4": 999,
    "Level1Bg5": 999,
    "Level1Bg6": 999,
    "FWizard": 200,
    "FWizardShot": 1,
    "LMage": 200,
    "LMageShot": 1,
    "Enemy": 100,
    "EnemyShot": 1
}

ENTITY_SHOT_DELAY = {
    "FWizard": 20,
    "LMage": 20,
    "Enemy": 60
}

# M
MENU_OPTION = ("NEW GAME 1P",
               "NEW GAME 2P",
               "SCORE",
               "EXIT")

# O
OUT_WIDTH = 1

# P
PLAYER_KEY_UP = {"FWizard": pygame.K_w,
                 "LMage": pygame.K_UP}
PLAYER_KEY_DOWN = {"FWizard": pygame.K_s,
                 "LMage": pygame.K_DOWN}
PLAYER_KEY_RIGHT = {"FWizard": pygame.K_d,
                 "LMage": pygame.K_RIGHT}
PLAYER_KEY_LEFT = {"FWizard": pygame.K_a,
                 "LMage": pygame.K_LEFT}
PLAYER_KEY_SHOOT = {"FWizard": pygame.K_f,
                    "LMage": pygame.K_SPACE}


# W
WIN_WIDTH = 800
WIN_HEIGHT = 450