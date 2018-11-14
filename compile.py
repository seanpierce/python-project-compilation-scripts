import os

from colorama import init
from colorama import Fore, Back, Style
init()

# declare file paths
AvellaSourceB_path = r"C:\Sites\Avella-SourceB\Avella_SourceB\App"

print(f'{Fore.GREEN}Get your compile on!{Style.RESET_ALL}')

while True:
    print("--------------------")
    print(f'{Fore.YELLOW}[1]{Style.RESET_ALL} Avella - SourceB')
    print(f'{Fore.YELLOW}[2]{Style.RESET_ALL} SonoraQuest')

    project = int(input("What project would you like to compile? "))

    if project == 1:
        print(f'{Fore.GREEN}Compiling: Avella - SourceB...{Style.RESET_ALL}')
        os.chdir(AvellaSourceB_path)
        os.system("gulp")
        break
    elif project != 1:
        print(f'{Fore.RED}That command is unavailable at this time.{Style.RESET_ALL}')
        continue
