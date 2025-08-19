#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import C_WHITE, MENU_OPTION, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode 
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("Level1Bg"))
        self.entity_list.append(EntityFactory.get_entity("FireWizard"))
        if game_mode in MENU_OPTION[0]:
            self.entity_list.append(EntityFactory.get_entity("Enemy"))
        if game_mode in MENU_OPTION[1]:
            self.entity_list.append(EntityFactory.get_entity("LMage"))

    def run(self, ):
        pygame.mixer_music.load("./asset/Level1Sound.mp3")
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            self.level_text(30, f"fps: {clock.get_fps():.0f}", C_WHITE, (40, WIN_HEIGHT - 20))

            pygame.display.flip()
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()   # Close window
                    quit()  # Encerrar o pygame
    

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)
