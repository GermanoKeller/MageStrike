#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.Const import ENTITY_SHOT_DELAY, ENTITY_SPEED, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.direction = -1
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centery += self.direction * ENTITY_SPEED[self.name]
        if self.rect.top <= WIN_HEIGHT / 2.5:
            self.direction = 1  # Muda para baixo
        if self.rect.bottom >= WIN_HEIGHT:
            self.direction = -1  # Muda

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f"{self.name}Shot", position=(self.rect.centerx, self.rect.centery - 20))
