# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

print(GREEN, "Cornel is the king of the Python")
print(" Well, I did not count on that.") # one needs to reset the special ANSI characters to print again in default colour


def colour_print(effect: str, text: str) -> None:
    """
    Prints in colours
    """
    print("{0}{1}{2}".format(effect, text, RESET))


colour_print(BLUE, "Wait...What?")