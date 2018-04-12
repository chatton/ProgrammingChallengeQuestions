"""

Build Tower
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

for example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]

"""


def tower_builder(n_floors):
    str_size = n_floors + n_floors - 1
    tower = []

    num_stars = 1
    for x in range(n_floors):
        list_str = ["*"] * num_stars

        while len(list_str) < str_size:
            list_str.append(" ")
            list_str.insert(0, " ")

        tower.append("".join(list_str))
        num_stars += 2

    return tower
