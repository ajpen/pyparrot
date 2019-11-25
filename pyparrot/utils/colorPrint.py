"""
Print messages in color

Messages are print to stderr to allow compatibility with the LeapDroneController, which communicates via STDIN/STDOUT
"""

import sys


def color_print(print_str, type="NONE"):
    # handle null cases
    if (print_str is None):
        print_str = ""

    if (type is "ERROR"):
        # red
        print('\033[38;5;196m %s \033[0m' % print_str, file=sys.stderr)

    elif (type is "WARN"):
        # orange
        print('\033[38;5;202m %s \033[0m' % print_str, file=sys.stderr)

    elif (type is "SUCCESS"):
        # green
        print('\033[38;5;22m %s \033[0m' % print_str, file=sys.stderr)

    elif (type is "INFO"):
        # blue
        print('\033[38;5;33m %s \033[0m' % print_str, file=sys.stderr)

    elif (type is "NONE" or type is "DEFAULT"):
        # black
        print('\033[0m %s \033[0m' % print_str, file=sys.stderr)
