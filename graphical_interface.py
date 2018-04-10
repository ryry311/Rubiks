from Cube import Cube
from graphics import *
from funcs import *

def display_cube(win, window_size, cube):
   tile_size = 40
   color_dict = {'f' : "blue", 'u' : "white", 'l' : "red", 'r' : "orange", 'b' : "green", 'd' : "yellow"}
  
   dx = .6
   dy = .7

   for item in win.items:
      win.delItem(item)

   for i in range(9):
      x = tile_size * ((i%3) + 1)
      y = window_size - (tile_size*4) + (tile_size * ((i//3) + 1))
      r = Rectangle(Point(x, y), Point(x + tile_size, y - tile_size)) 
      r.setFill(color_dict[eval('cube.front.row{}'.format(i//3 + 1))[i%3]])
      win.addItem(r)

   for i in range(9):
      x = tile_size * (i%3 + 1 + dx * (i//3))
      y = window_size - tile_size*(4 + (i//3)*dy)
      poly_list = [Point(x, y), Point(x + dx*tile_size, y - dy*tile_size), 
            Point(x + (1 + dx)*tile_size, y - dy*tile_size), Point(x + tile_size, y)]
      p = Polygon(poly_list)
      p.setFill(color_dict[eval('cube.up.row{}'.format(3 - i//3))[i%3]])
      win.addItem(p)

   for i in range(9):
      x = tile_size * (4 + dx * (i%3)) 
      y = window_size - tile_size * (1 + i//3 + (i%3) * dy) 
      poly_list = [Point(x, y), Point(x, y - tile_size), Point(x + dx*tile_size, y - (1 + dy)*tile_size), Point(x + dx*tile_size, y - (dy)*tile_size)]
      p = Polygon(poly_list)
      p.setFill(color_dict[eval('cube.right.row{}'.format(3 - i//3))[i%3]])
      win.addItem(p)

   for item in win.items:
      if not item.canvas:
         item.draw(win)


def main():
   window_size = 500
   win = GraphWin("Cube", window_size, window_size)

   cube = solved_cube()
   display_cube(win, window_size, cube)
   
   user_input = win.getKey() 
   while (move != 'q'):
      move(cube, user_input)
      print(user_input)
      display_cube(win, window_size, cube)
      user_input = win.getKey()
 
   win.close()

if __name__ == '__main__':
   main()
