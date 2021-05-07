#! /usr/bin/env python3
# coding: utf-8

class MenuEntry:

	def __init__(self, option, handler):
		self.option = option
		self.handler = handler

	def __repr__(self):
		return f"MenuEntry({self.option}, {self.handler})"

	def __str__(self):
		return str(self.option)


class Menu:
	def __init__(self):
		self._entries = {}
		self._autokey = 1  

	def add(self, key, option, handler):
		if key == "auto":
			key = str(self._autokey)
			self._autokey += 1

		self._entries[str(key)] = MenuEntry(option, handler)


if __name__ == "__main__":
	menu = Menu()
	menu.add("auto", "première option de menu", lambda: None)
	menu.add("auto", "seconde option du menu", lambda:None)
	menu.add("q", "dernière option du menu", lambda: None)
	print(menu._entries)