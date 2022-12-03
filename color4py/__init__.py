import fade
from color4py import system
from colorama import Fore
from enum import Enum

__AUTHOR__   = 'hayoto'
__VERSION__  = '1.0.1'
__LICENSE__  = 'MIT'

class Coloring:
    """
    Color your Text!
    """
    BLACK          = Fore.BLACK
    CYAN           = Fore.CYAN
    BLUE           = Fore.BLUE
    GREEN          = Fore.GREEN
    MAGENTA        = Fore.MAGENTA
    RED            = Fore.RED
    WHITE          = Fore.WHITE
    YELLOW         = Fore.YELLOW
    GRAY           = Fore.LIGHTBLACK_EX

    LIGHTGREEN     = Fore.LIGHTGREEN_EX
    LIGHTBLUE      = Fore.LIGHTBLUE_EX
    LIGHTMAGENTA   = Fore.LIGHTMAGENTA_EX
    LIGHTRED       = Fore.LIGHTRED_EX
    LIGHTYELLOW    = Fore.LIGHTYELLOW_EX
    LIGHTWHITE     = Fore.LIGHTWHITE_EX

class Effect(Enum):
    """
    Fade your Text!
    """
    BLACKWHITE = fade.blackwhite
    PURPLEPINK = fade.purplepink
    GREENBLUE = fade.greenblue
    WATER = fade.water
    YELLOWRED = fade.fire
    PINKRED = fade.pinkred
    PURPLEBLUE = fade.purpleblue
    BRAZIL = fade.brazil
    RANDOM = fade.random
