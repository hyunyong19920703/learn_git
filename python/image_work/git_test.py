import sys
import os
import mypy
import typing
from datetime import datetime

# print(sys.version)

# for i in sys.path:
#     print(i)


### @#

a = [1, 2, 3, 4, 5, 6]
b = [3, 4, 5, 6, 7, 8]

c = list(map(lambda x, y: x + y, a, b))

# print(c)


def add_numbers(a: int, b: int) -> int:
    return a + b

def test_jsDoc(a, b, c, d):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_
        c (_type_): _description_
        d (_type_): _description_

    Returns:
        _type_: _description_
    """
    return a+b+c+d

def get_time():
    return f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

class ABC(object):
    def __init__(self, name, data) -> None:
        self.name = name
        self.data = data
        self.created_at = get_time()
        
khy = ABC('hyuntong', 'lighting')

print(khy.created_at)
        