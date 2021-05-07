class Menu:
	def __init__(self):
		self._entries = {}

	def add(self, key, option, controller):
		if key == "auto":
			key = str(self._autokey)
			self._autokey += 1

		self._entries[str(key)] = (option, controller)
