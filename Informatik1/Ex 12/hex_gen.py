#!/usr/bin/env python3
from random import choice
class GameRunner(object):

    def __init__(self):
        self.rows = 17
        self.columns = 2

    def generate_hex_codes(self):
        chars = "0123456789ABCDEF"

        def rand():
            for _ in range(self.columns*self.rows):
                start = "0x"
                for _ in range(4):
                    start += choice(chars)
                yield start
        return list(rand())



