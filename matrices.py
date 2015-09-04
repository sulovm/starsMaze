from field import Cell


i = Cell.current.value
u = Cell.unreachable.value
w = Cell.water.value
x = Cell.x.value
h = Cell.health.value
e = Cell.energy.value
s = Cell.star.value
b = Cell.white.value

matrx1 = [[i, b, b, b, b, w, w, w, w, w],
          [u, u, u, u, b, b, b, b, b, s],
          [u, u, u, u, b, w, w, w, w, w],
          [s, u, u, u, b, b, b, b, b, s],
          [s, b, e, b, b, w, w, w, w, w],
          [s, u, u, u, b, b, b, b, b, s],
          [s, u, u, u, b, w, w, w, w, w],
          [u, u, u, u, b, b, b, h, b, s],
          [u, u, u, u, b, w, w, w, w, w],
          [e, s, s, b, b, b, b, b, b, b]]

matrx2 = [[i, b, b, b, b, b, w, w, w, w],
          [b, x, x, x, x, b, b, w, w, w],
          [b, x, s, e, x, w, b, w, w, w],
          [b, x, s, x, x, b, b, w, w, w],
          [b, b, b, u, u, s, b, s, s, s],
          [w, w, b, u, u, u, u, u, u, u],
          [s, w, b, u, u, u, u, u, u, u],
          [s, w, b, b, b, b, b, b, b, b],
          [b, b, b, b, b, x, x, x, s, b],
          [w, w, s, b, b, e, h, e, b, b]]

matrx3 = [[i, b, b, b, x, b, b, b, b, s],
          [u, u, u, u, u, u, b, u, u, u],
          [b, b, b, b, b, b, b, b, b, s],
          [b, u, u, b, b, x, x, x, e, w],
          [b, u, u, b, b, b, b, b, b, w],
          [b, b, u, b, b, w, b, w, b, w],
          [w, e, u, s, b, w, b, w, b, w],
          [s, e, u, b, b, b, s, b, b, h],
          [u, u, u, b, b, w, s, w, b, x],
          [s, s, s, b, b, w, s, w, b, b]]

matrx4 = [[i, b, b, b, b, b, b, b, b, b],
          [b, w, w, h, w, w, w, w, s, b],
          [b, w, w, w, w, b, b, w, w, b],
          [b, w, w, w, w, s, b, w, s, b],
          [b, b, b, b, b, u, b, s, w, b],
          [b, s, w, e, w, w, b, w, w, b],
          [b, w, w, x, w, w, s, s, e, b],
          [b, w, w, s, b, w, w, w, w, b],
          [b, s, w, w, b, w, w, s, w, b],
          [b, b, b, b, b, b, b, b, b, b]]

matrx5 = [[i, b, b, b, b, w, w, w, w, w],
          [u, u, u, u, x, h, b, b, b, s],
          [u, u, u, u, b, w, w, w, w, w],
          [s, u, u, u, b, b, b, b, b, s],
          [s, e, b, b, b, w, w, w, w, w],
          [s, u, u, u, b, b, b, b, b, s],
          [s, u, u, u, b, w, w, w, w, w],
          [u, u, u, u, b, h, b, b, b, s],
          [u, u, u, u, b, w, w, w, w, w],
          [e, s, s, b, b, b, b, b, b, b]]

matrx6 = [[i, b, b, b, b, b, b, b, b, b],
          [s, u, u, x, b, b, b, b, b, s],
          [w, w, x, b, b, w, x, b, b, w],
          [s, s, b, b, b, b, b, b, s, s],
          [x, x, x, x, x, b, x, x, x, x],
          [b, b, b, b, b, b, b, b, b, b],
          [b, b, u, u, u, u, u, u, u, b],
          [x, b, b, h, w, s, s, s, b, b],
          [b, b, u, u, u, u, u, u, u, b],
          [s, b, b, b, b, e, b, b, b, b]]

matrx7 = [[i, u, s, u, x, b, b, b, h, s],
          [b, u, s, u, w, b, u, u, u, u],
          [b, u, b, u, x, b, b, b, e, s],
          [b, u, b, u, w, b, u, u, u, u],
          [x, u, b, u, x, b, b, b, h, s],
          [b, b, b, u, b, b, u, u, u, u],
          [b, u, b, u, u, b, b, b, e, e],
          [b, u, s, b, b, b, w, w, w, b],
          [s, u, u, x, b, b, w, s, b, b],
          [h, u, u, s, s, w, w, e, w, b]]

matrx8 = [[i, b, b, h, w, s, u, s, h, s],
          [w, b, x, b, w, s, u, u, b, u],
          [w, x, b, b, w, b, x, b, b, e],
          [w, b, b, x, w, b, u, b, b, u],
          [w, b, x, b, w, b, u, b, w, s],
          [w, x, b, b, w, b, u, b, b, s],
          [e, b, b, b, b, b, u, b, w, s],
          [u, u, x, u, u, u, u, b, b, u],
          [s, b, b, b, b, b, b, b, x, b],
          [s, h, b, b, w, s, w, u, u, b]]

way_level1 = []
way_level2 = []
way_level3 = [{'place': [0, 4], 'way': ['r', 'r', 'r', 'r', 'l', 'l', 'l', 'l']}]
way_level4 = []
way_level5 = [{'place': [1, 4], 'way': ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'u', 'u', 'u', 'u', 'u', 'u', 'u']}]

way_level6 = [{'place': [1, 3], 'way': ['r', 'r', 'r', 'r', 'r', 'l', 'l', 'l', 'l', 'l']},
              {'place': [2, 2], 'way': ['r', 'r', 'l', 'l']},
              {'place': [2, 6], 'way': ['r', 'r', 'l', 'l']},
              {'place': [4, 4], 'way': ['r', 'l']},
              {'place': [7, 0], 'way': ['r', 'l']}]

way_level7 = [{'place': [4, 0], 'way': ['d', 'd', 'u', 'u']},
              {'place': [0, 4], 'way': ['r', 'r', 'l', 'l']},
              {'place': [2, 4], 'way': ['r', 'r', 'l', 'l']},
              {'place': [4, 4], 'way': ['r', 'r', 'l', 'l']},
              {'place': [8, 3], 'way': ['r', 'r', 'l', 'l']}]

way_level8 = [{'place': [1, 2], 'way': ['r', 'l', 'l', 'r']},
              {'place': [2, 1], 'way': ['r', 'r', 'l', 'l']},
              {'place': [2, 6], 'way': ['r', 'r', 'l', 'l']},
              {'place': [3, 3], 'way': ['l', 'l', 'r', 'r']},
              {'place': [4, 2], 'way': ['r', 'l', 'l', 'r']},
              {'place': [5, 1], 'way': ['r', 'r', 'l', 'l']},
              {'place': [7, 2], 'way': ['d', 'd', 'u', 'u']},
              {'place': [8, 8], 'way': ['r', 'l', 'l', 'r']}]

class Matrices:
    def __init__(self):
        self.matrices = [matrx1, matrx2, matrx3, matrx4, matrx5, matrx6, matrx7, matrx8]

class Ways:
    def __init__(self):
        self.ways = [way_level1, way_level2, way_level3, way_level4, way_level5, way_level6, way_level7, way_level8]
