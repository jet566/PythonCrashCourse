import pygame

class Ship:
	"""Klasa przeznaczona do zarządzania statkiem kosmicznym."""

	def __init__(self, ai_game):
		"""Inicjalizacja statku kosmicznego i jego położenie początkowe."""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Wczytanie obrazu statku kosmiczengo i pobranie jego prostokąta.
		self.image = pygame.image.load('images/ship.bmp')
		self.image = pygame.transform.scale(self.image, (80, 100))
		self.image = pygame.transform.rotate(self.image, -90)
		self.rect = self.image.get_rect()

		# Każdy nowy statek kosmiczny pojawia się na dole ekranu.
		self.rect.midleft = self.screen_rect.midleft

		# Położenie poziome statku jest przechowywane w postaci liczby zmiennoprzecinkowej.
		self.y = float(self.rect.y)

		# Opcje wskazujące na poruszanie się statku
		self.moving_down = False
		self.moving_up = False

	def update(self):
		"""
		Uaktualnienie położenia statku na podstawie opcji wskazującej jego ruch.
		"""
		# Uaktualnienie wartości współrzędnej Y statku, a nie jego prostokąta.
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.ship_speed

		# Uaktualnienie obietku rect na podstawie wartości self.x.
		self.rect.y = self.y


	def blitme(self):
		"""Wyświetlenie statku kosmicznego w jego aktualnym położeniu."""
		self.screen.blit(self.image, self.rect)



