import sys
import pygame

def check_events():
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()

def update_screen(ai_settings,screen,ship):
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	#让最近绘制的屏幕可见
	pygame.display.flip()
