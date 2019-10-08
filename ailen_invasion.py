#-*- encoding=utf-8 -*-
import sys
import pygame
from settings import Settings
from ship import Ship
from game_functions import check_events,update_screen
def run_game():
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	#bg_color=(80,120,200)
	ship=Ship(screen)
	#��ʼ��Ϸ����ѭ��
	while True:
		#���Ӽ��̺������¼�
		check_events()
		update_screen(ai_settings,screen,ship)
run_game()
