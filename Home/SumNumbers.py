"""
In a given text you need to sum the numbers. 
Only separated numbers should be counted. 
If a number is part of a word it shouldn't be counted.
The text consists from numbers, spaces and english letters
https://py.checkio.org/ru/mission/sum-numbers/
"""

import re


def sum_numbers(string):
    target = str(string)
    num_list = re.findall(r"-?\d", target)
    if len(num_list) == 0:
        return 0
    return sum(map(int, num_list))


assert sum_numbers("test") == 0  # Case 1
assert sum_numbers("1337") == 14  # Case 2
assert sum_numbers("1st move") == 1  # Case 3
assert sum_numbers("one 2 three 4") == 6  # Case 4
assert sum_numbers("William Ford Gibson (born March 17, 1948) is an American-Canadian speculative fiction writer and "
                   "essayist widely credited with pioneering the science fiction subgenre known as cyberpunk. "
                   "Beginning his writing career in the late 1970s, his early works were noir, near-future stories "
                   "that explored the effects of technology, cybernetics, and computer networks") == 47  # Case 5
assert sum_numbers("") == 0  # Case 6
assert sum_numbers("2, -1") == 1  # Case 7

assert sum_numbers(1) == 1  # Case 8
assert sum_numbers(1.4) == 5  # Case 9
