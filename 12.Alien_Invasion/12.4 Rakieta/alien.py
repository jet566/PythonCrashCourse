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

		# Każdy nowy obcy pojawi się na środku ekranu.
		self.rect.center = self.screen_rect.center

	def blitme(self):
		"""Wyświetlenie obcego w jego aktualnym położeniu."""
		self.screen.blit(self.image, self.rect)

