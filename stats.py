#coding:gb2312
class Stats():
	"""跟踪游戏统计信息"""
	def __init__(self,al_setting):
		"""初始化统计信息"""
		self.al_setting = al_setting
		self.reset_stats()
		self.game_active = True
	def reset_stats(self):
		"""初始化游戏中可能变化的信息"""
		self.people_life = self.al_setting.people_life
