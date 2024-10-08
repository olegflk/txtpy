# Небольшая программка для тестирования и проверки виртуального окружения Python `********************************************************************************************************************************************************************************`
# python3 -m venv .venv             - устанавливаем окружение
# source .venv/bin/activate         - активируем виртуальное окружение
# pip install -r requirements.txt   - настраиваем окружение- скачиваем недостающие библиотеки
#------------------------------------------------------
# импортируем библиотеки

# -- Проверяем версию python
import platform 
verpython = platform.python_version()
print('python_version = \033[01m', verpython, '\033[00m')

# = Активируем виртуальное окружение 
import os 
myCmd = "clear" 
os.system (myCmd)
#n = input('Press any key')
print('=================================================')
print ('\033[01;033m  source .venv/bin/activate \033[00m                - активировать виртуальное окружение') 
print ('\033[01;032m  python3 -m venv .venv \033[00m                    - установить виртуальную среду') 
print ('\033[01;036m  source .pip install -r requirements.txt \033[00m  - подгрузить модули и библиотеки') 
print('=================================================')
from rich import print
from rich.align import Align
from rich.console import Console
from rich.live import Live
from rich.table import Table

#---------------------------------------
# Приветствие
print ('=========================================')
print("[bold green] *** Hello! ***[/bold green]!")
print ('-----------------------------------------')
print ('Number - 1234567890 ; Symbol - ABCabc  ')
print ('Проверка работы  библиотеки [bold yellow]rich [/bold yellow]')
print ('========================================= ')
print ('Далее небольшой пример работы библиотеки  - Table')
print ('................................................')

TABLE_DATA = [
	[
		"[b blue]DSA Course[/]: [i]Beginner[/]",
		"[magenta]$[/]10",
		"[green]Geeks for Geeks[/]",
		"15 hours",
	],
	[
		"[b white]DSA Course[/]: [i]Intermediate[/]",
		"[magenta]$[/]20",
		"[green]Geeks for Geeks[/]",
		"25 hours",
	],
	[
		"[b white]DSA Course[/]: [i]Advanced[/]",
		"[magenta]$[/]30",
		"[green]Geeks for Geeks[/]",
		"30 hours",
	],
	[
		"[b white]Operating System Fundamentals[/]",
		"[magenta]$[/]25",
		"[green]Geeks for Geeks[/]",
		"35 hours",
	],
]

console = Console()


table = Table(show_footer=False)
table_centered = Align.center(table)

console.clear()

with Live(table_centered, console=console,
		screen=False):
	table.add_column("[b red]Course Name[/]", no_wrap=True)
	table.add_column("[b yellow]Price[/]", no_wrap=True)
	table.add_column("Organization", no_wrap=True)
	table.add_column("Duration", no_wrap=True)
	for row in TABLE_DATA:
		table.add_row(*row)

	table_width = console.measure(table).maximum

	table.width = None

# Приветствие
print ('=========================================')
print("[bold green] *** Hello! ***[/bold green]!")
print ('-----------------------------------------')
print ('Number - 1234567890 ; Symbol - ABCabc  ')
print ('Проверка работы  библиотеки [bold yellow]rich [/bold yellow]')
print ('========================================= \n')
print ('В центре таблица - [пример работы библиотеки ] - Table')
print ('................................................\n')

print ('deactivate') 





