import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet

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
		self.aliens = pygame.sprite.Group()
		self.bullets = pygame.sprite.Group()

	def run_game(self):
		"""Rozpoczęcie pętli głównej gry"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_aliens()
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
		if event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		# Zamknięcie gry po naciśnięciu klawisza 'q'.
		elif event.key == pygame.K_q:
			sys.exit()
		# Wystrzelenie pocisku
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		"""Reakcja na zwolnienie klawisza."""
		if event.key == pygame.K_DOWN:
			self.ship.moving_down = False
		elif event.key == pygame.K_UP:
			self.ship.moving_up = False

	def _fire_bullet(self):
		"""Utworzenie nowego pocisku i dodanie go do grupy pocisków."""
		if len(self.bullets) < self.settings.bullets_allowed:	
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Uaktualnienie położenia pocisków i usunięcie tych niewidocznych na ekranie."""
		# Uaktualnienie położenia pocisków.
		self.bullets.update()
		# Usunięcie pocisków, które znajdują się za ekranem
		for bullet in self.bullets.copy():
			if bullet.rect.left >= 1920:
				self.bullets.remove(bullet)

	def _create_fleet(self):
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_y = self.settings.screen_height - (alien_height * 2)
		number_aliens_y = available_space_y // (2 * alien_height)

		available_space_x = (self.settings.screen_width - (self.ship.rect.height - (2 * alien_width)))
		number_aliens_x = available_space_x // (2 * alien_height)
		number_rows = available_space_x // (2 * alien_height)

		for row_number in range(number_rows):
			for alien_number in range(number_aliens_y):
				self._create_alien(alien_number, row_number)

	def _create_alien(self, alien_number, row_number):
		alien = Alien(self)
		alien_width = alien.rect.width
		alien_height = alien.rect.height
		alien.y = alien_height + 2 * alien_height * alien_number
		alien.rect.x = alien.rect.width + 2 * alien.rect.width * row_number
		alien.rect.y = alien.y
		self.aliens.add(alien)

	def _update_aliens(self):
		self.aliens.update()

	def _check_fleet_edges(self):
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
			break

	def _change_fleet_direction(self):
		for alien in self.aliens.sprites():
			alien.rect.x -= self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _update_screen(self):
		"""Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
		self.screen.fill(self.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)
		# Przejście do nowego ekranu
		pygame.display.flip()


if __name__ == '__main__':
	# Utworzenie egzemplarza gry i jej uruchomienie.
	ai = AlienInvasion()
	ai.run_game()