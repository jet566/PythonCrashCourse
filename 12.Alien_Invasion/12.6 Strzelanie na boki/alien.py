import pygame

class Alien:
	"""Klasa przeznaczona do zarządzania obcym."""

	def __init__(self, ai_game):
		"""Inicjalizacja obcego i jego położenie początkowe."""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# Wczytanie obrazu obcego i pobranie jego prostokąta.
		self.image = pygame.image.load('images/alien.bmp')
		self.image = pygame.transform.scale(self.image, (70, 80))
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.y = float(self.rect.y)

	def update(self):
		self.y += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.y = self.y

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
			return True
