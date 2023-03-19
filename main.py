import requests

from json import load
from ui import UI

class Discord:

	def __convert(self) -> str:

		headers: dict = {'Authorization': config.get("token")}
		get_user = session.get(f"https://discord.com/api/users/{uid}", headers=headers).json()

		if "username" in get_user:
			username = get_user["username"] + "#" + get_user["discriminator"]
			return username
		else:
			return "Bad request"

	def _handle(self) -> None:

		username = self.__convert()

		if username != "Bad request":
			print(f"{ui.prefix} {ui.red}{uid}{ui.reset} -> {ui.red}{username}{ui.reset}")
		else:
			print(f"{ui.prefix} {ui.red}Bad request{ui.reset} while trying to convert {ui.red}{uid}{ui.reset}.")

def __user_input() -> int:

	uid = int(input(f"{ui.prefix} UID: "))

	return uid

def __load_config() -> dict:

	with open("config.json") as f:
		config = load(f)

	return config

if __name__ == "__main__":

	ui = UI()
	ui.clear()

	session = requests.Session()
	uid = __user_input()
	config = __load_config()
	discord = Discord()
	discord._handle()