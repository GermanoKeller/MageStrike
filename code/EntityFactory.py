#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player
from code.Const import WIN_HEIGHT, WIN_WIDTH

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case "Level1Bg":
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f"Level1Bg{i}", (0,0)))
                return list_bg
            case "FireWizard":
                return Player("FireWizard", (WIN_WIDTH/4, WIN_HEIGHT - 250))
            case "LMage":
                return Player("LMage", (WIN_WIDTH/1.4, WIN_HEIGHT - 250))
            case "Enemy":
                return Enemy("LMage", (WIN_WIDTH/1.4, WIN_HEIGHT - 250))