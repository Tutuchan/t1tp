# t1tp

A Python tool to retrieve Time-based One Time Passwords from a 1Password account.

## Prerequisites

+ Python3
+ A 1Password.com account
+ the `op` commmand line tool: `brew cask install 1password-cli`

## Installation

```
git clone https://github.com/tutuchan/t1tp .
cd t1tp
pip install .
```

## Usage

```
usage: t1tp [-h] [-c] [-g ITEM] [-v]

optional arguments:
  -h, --help           show this help message and exit
  -c, --check          check that t1tp is setup correctly
  -g ITEM, --get ITEM  the title of the 1Password item to retrieve the OTP
                       from
  -v, --verbose        show more information
```

The first time you run the command, you may be asked to enter your 1Password email and master key (needed by `op`), then your password twice.

After that, you will only be asked for your password and a token will be created for the session. These tokens last 30 minutes.