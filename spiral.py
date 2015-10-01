import sys
import pickle
from collections import deque


# import the already existing data
try:
    f = open('coordinate_list', 'r')
    data = list(map(eval,  f.readlines()))
    f.close()
    data = deque(data)
except:
    data = deque([(0, 0), ])  # the first number is at 0, 0
# set global values
coordinate = (0, 0)
index = 0.0
limit = 0


# now start the spiraler
def move(current):
    "moves coordinate in current direction"
    global data, index
    global coordinate
    x, y = coordinate
    d = {'u': (x, y+1),
         'd': (x, y-1),
         'r': (x+1, y),
         'l': (x-1, y)
         }
    coordinate = d[current]
    save(coordinate)
    index += 1
    if index > limit:
        save()
        sys.exit(0)


def save(x):
    with open('coordinate_list', 'a') as f:
        f.write(str(x) + '\n')


def spiral_gen(l=int(1e6)):
    "generate the spiral"
    repeat = 0
    current = 'u'
    nxt = {'u': 'r',
           'r': 'd',
           'd': 'l',
           'l': 'u'
           }
    global limit
    limit = int(l * l)
    for count in range(limit):
        repeat += 1
        move(current)
        if index % 10 == 0:
            print(round(index/limit, 2), end='\r')
        for i in range(2):
            current = nxt[current]
            for j in range(repeat):
                move(current)


if __name__ == '__main__':
    limit = int(input('Enter length of side of square to generate: '))
    spiral_gen(limit)
