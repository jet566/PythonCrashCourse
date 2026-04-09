class Settings:
	"""Klasa przeznaczona do przechowywania wszystkich ustawień gry."""

	def __init__(self):
		"""Inicjalizacja ustawień gry."""

		# Ustawienia ekranu.
		self.screen_width = 1920
		self.screen_height = 1080
		self.bg_color = (207, 232, 249)
		# Ustawienia statku.
		self.ship_speed = 1.5
		# Ustawienia dotyczące pocisków.
		self.bullet_speed = 1.0
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 7

		self.alien_speed = 1.0
		self.fleet_drop_speed = 5

		self.fleet_direction = 1
