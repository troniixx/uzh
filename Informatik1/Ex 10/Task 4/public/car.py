#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from abc import ABC, abstractmethod

class Car:

    @abstractmethod
    def get_remaining_range(self):
        pass

    @abstractmethod    
    def drive(self, dist):
        pass
