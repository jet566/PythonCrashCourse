class Settings:
	"""Klasa przeznaczona do przechowywania wszystkich ustawień gry."""

	def __init__(self):
		"""Inicjalizacja ustawień gry."""

		# Ustawienia ekranu.
		self.screen_width = 1920
		self.screen_height = 1080
		self.bg_color = (207, 232, 249)
		self.ship_speed = 1.5