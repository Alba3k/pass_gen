import random, time
from colorama import Fore, Back, Style
from colorama import init
from rich.console import Console
from rich.table import Table

console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("№ п/п", style="yellow", width=15)
table.add_column("Пароль", style="green", width=50, justify="left")

# инициализация библиотеки colorama
init()
MENU = """

	██████╗  █████╗ ███████╗███████╗               ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
	██╔══██╗██╔══██╗██╔════╝██╔════╝              ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
	██████╔╝███████║███████╗███████╗    █████╗    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
	██╔═══╝ ██╔══██║╚════██║╚════██║    ╚════╝    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
	██║     ██║  ██║███████║███████║              ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
	╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝               ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

	Программа для генерации паролей.
	Используемые команды:

	help 	- помощь о программе
	pass 	- генерация паролей
	print	- вывод паролей на экран
	save	- сохранение паролей в файл password.txt
	exit 	- выход из программы                                                                         
"""
HELP = """
Программа для генерации паролей в различных комбинациях.
Сгенерированные пароли сохраняются в текстовой файл. 
Написана с использованием языка программирования Python 3.9. 
и модулей: colorama, random, time, rich.
Разработчик AlBa3k @ 2021
"""
# Функция генерации паролей на основе латинского алфавита и спецсимволов
def good_pass_gen(length):
	alphabet = ('qwertyuiopasdfghjklzxcvbnm'
				'QWERTYUIOPASDFGHJKLZXCVBNM'
				'1234567890-=<>?!@#$%^&*()'
				)
	password = ''
	for i in range(length):
		password += random.choice(alphabet)
	return password

print(MENU)

while True:
	command = input("Введите Вашу команду: ")	
	if command == 'help':
		print(HELP)

	elif command == 'pass':
		length_pass = int(input('Введите длину пароля в символах: '))
		q_ty_pass = int(input('Количество сгенерированных паролей: '))
		print('')
		list_password = []
		for x in range(q_ty_pass):
			password = good_pass_gen(length_pass)
			list_password.append(password)
		print('Пароли созданы.')

	elif command == 'print':
		for i,v in enumerate(list_password,1):
			table.add_row("Пароль № " + str(i), str(v))
		console.print(table)

	elif command == 'save':
		timestr = time.strftime('%H%M%S')
		passfile_name = 'password_' + timestr + '.txt'
		for idx, val in enumerate(list_password):
			f = open(passfile_name, "a+", encoding="utf8")
			f.write(f"Пароль № {int(idx)+1} : {val}" + "\r\n")
		print(f'Пароли сохранены в файле {passfile_name}.')

	elif command == 'exit':
		console.print('Спасибо за использование Pass-Generator. До свидания!', style="green")
		break

	else:
		console.print('Введите правильную команду.', style="red")