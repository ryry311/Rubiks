from Cube import Cube
from funcs import *

def main():
   c = solved_cube()
   shuffle(c)

   while (c.cost() > 25):
      n = c.cost()
      l = [0]
      reduce_cost(c, n - 1, l)
      print(c.cost())
   
   print(l[0])
   c.print_cube()
   #user interface
   '''user_input = input("Enter move: ")
   move(c, user_input)
   c.print_cube()
   num_moves = 1
   
   while(c.cost != 0 and move != 'q'):
      user_input = input("Enter move: ")
      move(c, user_input)
      num_moves += 1

   if (move == q):
      print('Good luck next time!')
   else:
      print('Congratulations! You solved the cube in {} moves.'.format(num_moves))'''

if __name__ == '__main__':
   main()
