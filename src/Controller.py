#!/usr/bin/python

import sys
from application.RegexGenerator import RegexGenerator

INFORMATION_MESSAGE = "You must specify a numbers list comma separated, like: 123456,456789,456789"
if len(sys.argv) < 2:
    raise ValueError(INFORMATION_MESSAGE)

regex_generator = RegexGenerator()

try:
    phones_list = list(map(int, str(sys.argv[1]).split(',')))
except ValueError:
    raise ValueError(INFORMATION_MESSAGE)

regex = regex_generator.build_phones_regex(phones_list)

