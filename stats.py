#coding:gb2312
class Stats():
	"""������Ϸͳ����Ϣ"""
	def __init__(self,al_setting):
		"""��ʼ��ͳ����Ϣ"""
		self.al_setting = al_setting
		self.reset_stats()
		self.game_active = True
	def reset_stats(self):
		"""��ʼ����Ϸ�п��ܱ仯����Ϣ"""
		self.people_life = self.al_setting.people_life
