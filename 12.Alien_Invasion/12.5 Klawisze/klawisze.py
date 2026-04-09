import pygame
import sys

class Game():
	def __init__(self):
		pygame.init()
		self.screen_width = 1280
		self.screen_height = 840
		self.bg_color = (40, 190, 200)
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
	def run_game(self):
		while True:
			self._check_events()
			self._update_screen()


	def _update_screen(self):
		self.screen.fill(self.bg_color)
		pygame.display.flip()

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

	def _check_keydown_events(self, event):
		print(event.key)
		if event.key == pygame.K_q:
			sys.exit()


if __name__ == '__main__':
	g = Game()
	g.run_game()