import fade
from color4py import system
from colorama import Fore

__AUTHOR__   = 'hayoto'
__VERSION__  = '1.0.0'
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

class Fade:
    """
    Fade your Text!
    """
    def blackwhite(text):
        return fade.blackwhite(text)
    def purplepink(text):
        return fade.purplepink(text)
    def greenblue(text):
        return fade.greenblue(text)
    def water(text):
        return fade.water(text)
    def yellowred(text):
        return fade.fire(text)
    def pinkred(text):
        return fade.pinkred(text)
    def purpleblue(text):
        return fade.purpleblue(text)
    def greenyellow(text):
        return fade.brazil(text)
    def glitch(text):
        return fade.random(text)