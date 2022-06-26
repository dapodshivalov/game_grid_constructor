from typing import NamedTuple, TypeVar


class Pair(NamedTuple):
    first: str
    second: str

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Pair):
            return self.first in other and self.second in other and len(self) == len(other)
        return False
