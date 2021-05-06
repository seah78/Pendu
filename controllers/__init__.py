from ..views import  HomeMenuView
from ..models import Menu


class ApplicationController:

	def __init__(self):
		self.controller = None


	def start(self):
		self.controller = HomeMenuController
		while self.controller:
			self.controller = self.controller()

	

class HomeMenuController:
	def __init__(self):
		self.menu = Menu()
		self.view = HomeMenuView()

	def __call__(self):
		# 1. Construire un menu
		self.menu.add("auto", "Se connecter", ConnectionMenuController())
		self.menu.add("auto", "Commencer une partie", NewGameController())
		self.menu.add("q", "Quitter", EndScreenController())

		# 2. Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur
		user_choice = self.view.get_user_choice()

		# 3. Retourner le controller associé au chois de l'utilisateur au contrôleur principal
		return user_choice.controller

class ConnectionMenuController:
	def __call__(self):
		return # controlleur suivant

class SignupMenuController:
	pass

class  NewGameController:
	pass


class OnGoingGameController:
	pass

class RankingController:

	pass

class EndScreenController:
	pass


if __name__ == "__main__":
	app = ApplicationController()
	app.start()

	