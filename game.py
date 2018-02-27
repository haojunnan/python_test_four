#coding:gb2312
import pygame
import functions as gf
from settings import Settings
from pygame.sprite import Group
from ball import Ball
from people import People
from stats import Stats
def rungame():
	#初始化
	pygame.init()
	al_setting = Settings()
	#创建窗口
	screen = pygame.display.set_mode((al_setting.screen_width,
	al_setting.screen_height))
	pygame.display.set_caption("catch the ball")
	stats = Stats(al_setting)
	#创建角色
	people = People(al_setting,screen)
	#创建球组
	balls = Group()
	#创建角色组
	peoples = Group()
	peoples.add(people)
	while True:
		#鼠标键盘相应事件
		gf.check_event(people)
		if stats.game_active:	
			#更新角色位置
			people.update()
			#更新球的位置
			gf.ball_update(al_setting,screen,balls,peoples,stats)
			#刷新界面
		gf.screen_update(al_setting,screen,balls,people)
rungame()
