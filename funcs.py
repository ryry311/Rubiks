import random
import Cube, Side

def move(cube, m):
   if m == 'f':
      cube.F()
   elif m == 'd':
      cube.D()
   elif m == 'r':
      cube.R()
   elif m == 'l':
      cube.L()
   elif m == 'b':
      cube.B()
   elif m == 'u':
      cube.U()
   elif m == 'F':
      cube.Fi()
   elif m == 'D':
      cube.Di()
   elif m == 'R':
      cube.Ri()
   elif m == 'L':
      cube.Li()
   elif m == 'B':
      cube.Bi()
   elif m == 'U':
      cube.Ui()
   elif m == 'Right':
      cube.view_change_right()
   elif m == 'Left':
      cube.view_change_left()
   elif m == 'Up':
      cube.view_change_up()
   elif m == 'Down':
      cube.view_change_up()

def shuffle(cube, n=100):
   moves = ['f', 'd', 'r', 'l', 'b', 'u', 'F', 'D', 'L', 'B', 'U', 'R']
   for i in range(n):
      move(cube, random.choice(moves))

def solved_cube():
   return Cube.Cube(Side.Side('f'), Side.Side('r'), Side.Side('u'), Side.Side('l'), Side.Side('b'), Side.Side('d'))

def reduce_cost(cube, n, l):
   moves = ['f', 'd', 'r', 'l', 'b', 'u', 'F', 'D', 'L', 'B', 'U', 'R']
   while cube.cost() > n:
      l[0] += 1
      move(cube, random.choice(moves))

