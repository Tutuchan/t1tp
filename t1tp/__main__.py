#!/usr/bin/env python

import sys
import argparse
from t1tp.t1tp import OnePassword


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--check", help="check that t1tp is setup correctly", action="store_true")
    parser.add_argument("-g", "--get", help="the title of the 1Password item to retrieve the OTP from", metavar="ITEM")
    parser.add_argument("-v", "--verbose", help="show more information", action="store_true")

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    op = OnePassword(verbose=args.verbose)

    if args.check:
        if op.check_op_config():
            sys.exit(0)
        else:
            op.signin_first_time()


    op.signin()

    try:
        token = op.get_token(args.get)
    except TypeError:
        sys.exit(1)

    print(token)
    sys.exit(0)


if __name__ == '__main__':
    main()
