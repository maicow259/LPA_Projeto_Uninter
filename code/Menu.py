#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./assets/menu/bg_menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            pygame.display.flip()
        pass
