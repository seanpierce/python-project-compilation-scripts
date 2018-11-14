from colorama import init
from colorama import Fore, Back, Style
init()


def green(string):
    return f'{Fore.GREEN}' + string + f'{Style.RESET_ALL}'


def yellow(string):
    return f'{Fore.YELLOW}' + string + f'{Style.RESET_ALL}'


def red(string):
    return f'{Fore.RED}' + string + f'{Style.RESET_ALL}'
