# t1tp

A Python tool to retrieve Time-based One Time Passwords from a 1Password account.

## Prerequisites

+ Python3
+ A 1Password.com account
+ the `op` [commmand line tool](https://app-updates.agilebits.com/product_history/CLI): install it and move it to your path

## Installation

```
git clone https://github.com/tutuchan/t1tp .
cd t1tp
pip install .
```

## Usage


```
t1tp "<item>"
```

The first time you run the command, you may be asked to enter your 1Password email and master key (needed by `op`), then your password twice.

After that, you will only be asked for your password and a token will be created for the session. These tokens last 30 minutes.