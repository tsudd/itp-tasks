import re

MAIL_REGEX = '[^ ]+@[\w]+.[\w]+'
FLOAT_REGEX = '^[\d]+.?[\d]*$'
URL_REGEX = '^(?P<scheme>[\w]+)://((?P<host>[\d.]+):(?P<port>[\d]{4}))?(?P<path>[^\s #&?]+)(?P<parameters>\?' \
            '((?P<parameter>[\w\d]+)=(?P<value>[^=&]+))(\&((?P<npar>[\w\d]+)=(?P<nvalue>[^=&]+))+)+)?'

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


