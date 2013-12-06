#!/usr/bin/env python


def handle_one():
    return 'one'


def handle_two():
    return 'two'


def handle_default():
    return 'unknown'
cases = {
    'one': handle_one,
    'two': handle_two,
    'three': lambda: 'three',
}
for i in ('one', 'two', 'three', 'four', ):
    handler = cases.get(i, handle_default)
    print(handler)