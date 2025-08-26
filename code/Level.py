#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import C_GREEN, C_WHITE, MENU_OPTION, WIN_HEIGHT
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode 
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("Level1Bg"))
        self.entity_list.append(EntityFactory.get_entity("FWizard"))
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
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == "FWizard":
                    self.level_text(20, f"FireWizard - Health:{ent.health}", C_GREEN, (90, WIN_HEIGHT - 430))
                if ent.name == "LMage":
                    self.level_text(20, f"LightningMage - Health:{ent.health}", C_GREEN, (700, WIN_HEIGHT - 430))
            self.level_text(20, f"fps: {clock.get_fps():.0f}", C_WHITE, (30, WIN_HEIGHT - 20))

            pygame.display.flip()

            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()   # Close window
                    quit()  # Encerrar o pygame

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, outline_color=(0,0,0), outline_width=1):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_pos)

        # Render outline
        if outline_width > 0:
            outline_surf = text_font.render(text, True, outline_color).convert_alpha()
            for dx in range(-outline_width, outline_width+1):
                for dy in range(-outline_width, outline_width+1):
                    if dx != 0 or dy != 0:
                        outline_rect = outline_surf.get_rect(center=(text_pos[0]+dx, text_pos[1]+dy))
                        self.window.blit(source=outline_surf, dest=outline_rect)

        self.window.blit(source=text_surf, dest=text_rect)
