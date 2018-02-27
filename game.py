#coding:gb2312
import pygame
import functions as gf
from settings import Settings
from pygame.sprite import Group
from ball import Ball
from people import People
from stats import Stats
def rungame():
	#��ʼ��
	pygame.init()
	al_setting = Settings()
	#��������
	screen = pygame.display.set_mode((al_setting.screen_width,
	al_setting.screen_height))
	pygame.display.set_caption("catch the ball")
	stats = Stats(al_setting)
	#������ɫ
	people = People(al_setting,screen)
	#��������
	balls = Group()
	#������ɫ��
	peoples = Group()
	peoples.add(people)
	while True:
		#��������Ӧ�¼�
		gf.check_event(people)
		if stats.game_active:	
			#���½�ɫλ��
			people.update()
			#�������λ��
			gf.ball_update(al_setting,screen,balls,peoples,stats)
			#ˢ�½���
		gf.screen_update(al_setting,screen,balls,people)
rungame()
