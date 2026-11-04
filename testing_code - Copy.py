import math
from abc import ABC, abstractmethod


class x(ABC):
    @abstractmethod
    def generate(self):
        """Return a random float between 0 and 1."""
        return math.random()

    @abstractmethod
    def describe(self):
        """Return a readable description of the generated value."""
        return f"Random value: {self.generate():.4f}"

    @abstractmethod
    def scaled(self, scale):
        """Scale the generated value by the given multiplier."""
        return self.generate() * scale


class RandomX(x):
    def generate(self):
        return math.random()

    def describe(self):
        return f"Random value: {self.generate():.4f}"

    def scaled(self, scale):
        return self.generate() * scale


value = RandomX()
print(value.generate())
print(value.describe())
print(value.scaled(100))