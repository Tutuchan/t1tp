#!/usr/bin/env python

import sys
from t1tp.t1tp import OnePassword


def main():

    def usage():
        return 'Usage: {0} <service>'.format(sys.argv[0])

    op = OnePassword()
    op.signin()

    try:
        token = op.get_token(sys.argv[1])
    except Exception as e:
        print(usage())
        sys.exit(1)

    print(token)
    sys.exit(0)


if __name__ == '__main__':
    main()
