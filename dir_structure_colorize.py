import sys
from colorama import Fore, Back, Style
from pathlib import Path

def get_path():
    path = Path(sys.argv[1]) if (len(sys.argv) >= 2) and (Path(sys.argv[1]).exists()) else Path('')
    return path

def print_structure(path, offset=""):
    path_items = path.iterdir()
    for item in path_items:
        if item.is_dir():
            print(f"{offset} {Style.BRIGHT} {Fore.RED}      > {Back.RED} {item.name} {Style.RESET_ALL}")
            path = item.absolute()
            print_structure(path, offset + " "*4)
        else: 
            print(f"{offset} {Style.BRIGHT} {Fore.BLUE}      > {Back.BLUE} {item.name} {Style.RESET_ALL}")

def dir_structure_colorize():
    path=get_path()
    print(f"{Back.GREEN} {path} {Style.RESET_ALL}")
    print_structure(path)

dir_structure_colorize()

