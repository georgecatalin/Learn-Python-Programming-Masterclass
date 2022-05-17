import colorama

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


def colour_print(text: str, *effects: str) -> None:
    """
    Args:
        text: The text to print in colours
        *effects: One or more effects to include from considering the escape characters
    Returns: Nothing
    """
    effect_cumulated = "".join(effects)
    print("{0}{1}{2}".format(effect_cumulated, text,  RESET))


colorama.init()
colour_print("Cornel purchases crypto.", GREEN, REVERSE)
colour_print("He is the warrior of Kent", UNDERLINE, RED)

colorama.deinit()