#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_BLACK, C_LIGHT_YELLOW, C_WHITE, MENU_OPTION, OUT_WIDTH, WIN_WIDTH

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/BMenu.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self, ):
        pygame.mixer_music.load("./asset/menuSound.wav")
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(150, "MageStrike", C_LIGHT_YELLOW, ((WIN_WIDTH/2), 120))
            # Escreve o menu
            for i in range(len(MENU_OPTION)):
                self.menu_text(50, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH/2), 350 + 50*i))
                
            pygame.display.flip()

             # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()   # Close window
                    quit()  # Encerrar o pygame
                
    
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        outline_width = OUT_WIDTH # Define the outline width
        outline_color = C_BLACK  # Define o outline color

        # Renderiza o contorno em volta do texto
        outline_surf: Surface = text_font.render(text, True, outline_color).convert_alpha()
        outline_rect: Rect = outline_surf.get_rect(center=text_center_pos)

        # Desenha o contorno em volta do texto
        for dx in range(-outline_width, outline_width + 1):
            for dy in range(-outline_width, outline_width + 1):
                if dx != 0 or dy != 0:
                    offset_rect = outline_rect.copy()
                    offset_rect.centerx += dx
                    offset_rect.centery += dy
                    self.window.blit(outline_surf, offset_rect)

        # Renderiza e desenha o texto principal
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
