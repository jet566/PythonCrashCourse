import pygame
from pygame.sprite import Sprite

class Star(Sprite):
	"""Klasa przedstawiająca obcego we flocie."""

	def __init__(self, s_game):
		"""Inicjalizacja obcego i jego położenie początkowe."""
		super().__init__()
		self.screen = s_game.screen

		# Wczytanie obrazu obcego i pobranie jego prostokąta.
		self.image = pygame.image.load('images/star.png')
		self.image = pygame.transform.scale(self.image, (5, 5))
		self.rect = self.image.get_rect()

		# Umieszczenie nowego obcego w pobliżu lewego górnego rogu ekranu.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Przechowywanie dokładnego poziomego położenia obcego.
		self.x = float(self.rect.x)
