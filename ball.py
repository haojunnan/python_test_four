#coding:gb2312
import pygame
from pygame.sprite import Sprite
from random import randint
class Ball(Sprite):
	"""创建球"""
	def __init__(self,al_setting,screen):
		"""初始化"""
		super(Ball,self).__init__()
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.al_setting = al_setting
		self.image = pygame.image.load("ball.bmp")
		self.rect = self.image.get_rect()
		self.rect.y = self.rect.height
		self.rect.x = randint(0,al_setting.screen_width - self.rect.width)
		self.y = float(self.rect.y)
	def check_edge(self):
		"""判断是否到达边界"""
		if self.rect.bottom > self.screen_rect.bottom:
			return True
	def update(self):
		"""更新位置"""
		self.y += self.al_setting.ball_speed
		self.rect.y = self.y
