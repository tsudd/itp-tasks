import re

MAIL_REGEX = '[^ ]+@[\w]+.[\w]+'


def solve():
    print("Starting of the program\nInput \'q\' after \':\' to exit.")
    puted = ''
    while True:
        try:
            puted = str(input())
        except Exception:
            print("Wrong input. Try again.")
            continue

        if puted.startswith(':'):
            if puted == ":q":
                break

        if not re.match(MAIL_REGEX, puted) is None:
            print("MAIL")
        else:
            print("Not MAIL")
    print("Good luck.")


