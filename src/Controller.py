#!/usr/bin/python

import sys
from application.RegexGenerator import RegexGenerator as regex_generator


if (len(sys.argv) < 2):
    raise ValueError("You must specify a numbers list comma separated, like: 123456,456789,456789")

phones_list = list(map(int, str(sys.argv[1]).split(',')))

for phone in phones_list:
    regex = regex_generator.build_phone_regex(phone)
    print(repr(regex))

