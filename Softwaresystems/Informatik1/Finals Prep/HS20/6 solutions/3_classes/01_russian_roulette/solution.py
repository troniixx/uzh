#!/usr/bin/env python3

import random

class Revolver:
    def __init__(self, cylinder_size):
        self.cylinder_size = cylinder_size
        self.reload()

    def reload(self):
        self.bullets = [True] + ([False] * (self.cylinder_size - 1))
        random.shuffle(self.bullets)

    def trigger(self):
        if self.bullets and self.bullets.pop():
            return "BANG!!!"
        return "Click!"

