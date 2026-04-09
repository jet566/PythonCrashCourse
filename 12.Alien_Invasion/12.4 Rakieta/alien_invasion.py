import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien

class AlienInvasion:
	"""Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry."""

	def __init__(self):
		"""Inicjalizacja gry i utworzenie jej zasobów."""
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		# Zdefiniowanie nazwy na pasku tytułowym
		pygame.display.set_caption("Inwazja obcych")
		# Zdefiniowanie koloru tła.
		self.bg_color = (self.settings.bg_color)
		# Stworzenie egz. klasy Ship
		self.ship = Ship(self)
		self.alien = Alien(self)

	def run_game(self):
		"""Rozpoczęcie pętli głównej gry"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_screen()

	def _check_events(self):
		"""Reakcja na zdarzenie generowane przez klawiaturę i mysz."""
		for event in pygame.event.get():
				# Reakcja na zamknięcie gry.
				if event.type == pygame.QUIT:
					sys.exit()
				# Reakcja na naciśnięcie klawisza.
				elif event.type == pygame.KEYDOWN:
					self._check_keydown_events(event)
				# Reakcja na zwolnienie klawisza.
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Reakcja na naciśnięcie klawisza."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		if event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		# Zamknięcie gry po naciśnięciu klawisza 'q'.
		elif event.key == pygame.K_q:
			sys.exit()

	def _check_keyup_events(self, event):
		"""Reakcja na zwolnienie klawisza."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		if event.key == pygame.K_DOWN:
			self.ship.moving_down = False
		elif event.key == pygame.K_UP:
			self.ship.moving_up = False


	def _update_screen(self):
		"""Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
		self.screen.fill(self.bg_color)
		self.ship.blitme()
		self.alien.blitme()
		# Przejście do nowego ekranu
		pygame.display.flip()


if __name__ == '__main__':
	# Utworzenie egzemplarza gry i jej uruchomienie.
	ai = AlienInvasion()
	ai.run_game()