#coding:gb2312
import pygame
import sys
from ball import Ball
def key_down(event,people):
	if event.key == pygame.K_RIGHT:
		people.moving_right = True
	elif event.key == pygame.K_LEFT:
		people.moving_left = True
	elif event.key == pygame.K_UP:
		people.moving_up = True
	elif event.key == pygame.K_DOWN:
		people.moving_down = True
def key_up(event,people):
	if event.key == pygame.K_RIGHT:
		people.moving_right = False
	elif event.key == pygame.K_LEFT:
		people.moving_left = False
	elif event.key == pygame.K_UP:
		people.moving_up = False
	elif event.key == pygame.K_DOWN:
		people.moving_down = False
def check_event(people):
	"""鼠标键盘相应事件"""
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			key_down(event,people)
			if event.key == pygame.K_ESCAPE:
				sys.exit()
		elif event.type == pygame.KEYUP:
			key_up(event,people)
		elif event.type == pygame.QUIT:
			sys.exit()	
def ball_update(al_setting,screen,balls,peoples,stats):
	"""判断是否有球，产生新球，更新球的位置"""
	ball = Ball(al_setting,screen)
	balls.update()
	if len(balls) == 0:
		balls.add(ball)
	for ball in balls:
		#如果到边缘，移除球，life-1
		if ball.check_edge():
			balls.remove(ball)
			lose_ball(stats)
	#如果接到球，移除球
	collisions = pygame.sprite.groupcollide(peoples,balls,False,True)
def lose_ball(stats):
	if stats.people_life > 0:
		stats.people_life -= 1
	else:
		stats.game_active = False
def screen_update(al_setting,screen,balls,people):
	"""刷新界面"""
	screen.fill(al_setting.bg_color)
	people.blitme()
	balls.draw(screen)
	pygame.display.flip()
