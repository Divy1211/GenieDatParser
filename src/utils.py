from typing import TypeVar

T = TypeVar('T')

def log_it(t: T) -> T:
    print(t)
    return t
