#coding:gb2312
import pygame
from pygame.sprite import Sprite
class People(Sprite):
	def __init__(self,al_setting,screen):
		"""初始化，设定人的图像和位置"""
		super(People,self).__init__()
		self.al_setting = al_setting
		self.screen = screen
		self.image = pygame.image.load("people.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.centerx = float(self.rect.centerx)
		self.bottom = float(self.rect.bottom)
	def update(self):
		"""根据状态调整人的位置"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.al_setting.people_speed
		elif self.moving_left and self.rect.left > self.screen_rect.left:
			self.centerx -= self.al_setting.people_speed
		elif self.moving_up and self.rect.top > 0:
			self.bottom -= self.al_setting.people_speed
		elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.bottom += self.al_setting.people_speed
		self.rect.centerx = self.centerx
		self.rect.bottom = self.bottom
	def blitme(self):
		"""在屏幕上绘制人物"""
		self.screen.blit(self.image,self.rect)
