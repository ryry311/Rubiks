#All pieces of a Rubiks cube are either a Corner(3 colors), an Edge(2 colors), or a Middle(1 color)
#Middles never move - white is always up, yellow down, orange/blue/red/green sides in that order
#Colors are one of: (u)p, (d)own, (f)ront, (b)ack, (l)eft, ()right

#This needs to be WAY faster

class Corner:
   #There are 8 corners. a corner is either on the top side or the bottom side
   # "left" and "up" means if you orient the cube s.t. the piece is in the upper left corner
   def __init__(self, is_up, facing_color, left_color, up_color):
      self.is_up = is_up #bool
      self.facing_color = facing_color
      self.left_color = left_color
      self.up_color = up_color

class Edge:
   #12 edges. edges can be on up, down, or middle layer
   #if edge is on top or bottom, color1 is the facing color
   #otherwise, color1 is the counterclockwise color
   def __init__(self, layer, color1, color2):
      self.layer = layer
      self.color1 = color1
      self.color2 = color2

#IDK if the "is_up" and "layer" parameters will be useful yet
corner_set = [Corner(True, 'u', 'l', 'b'),#
              Corner(True, 'u', 'b', 'r'),#
              Corner(True, 'u', 'f', 'l'),
              Corner(True, 'u', 'r', 'f'),

              Corner(False, 'd', 'l', 'f'),
              Corner(False, 'd', 'f', 'r'),
              Corner(False, 'd', 'b', 'l'),#
              Corner(False, 'd', 'r', 'b')]#

edge_set = [Edge('up', 'u', 'b'),#
            Edge('up', 'u', 'l'),
            Edge('up', 'u', 'r'),
            Edge('up', 'u', 'f'),
            
            Edge('down', 'd', 'f'),  
            Edge('down', 'd', 'l'),  
            Edge('down', 'd', 'r'),  
            Edge('down', 'd', 'b'),# 

            Edge('mid', 'f', 'l'),
            Edge('mid', 'r', 'f'),
            Edge('mid', 'l', 'b'),#
            Edge('mid', 'b', 'r')]#

class Cube:
   #Position matters. corner_arr = [topQ2, topQ1, topQ3, topQ4, underQ2, underQ1, underQ3, underQ4] (Q meaning quadrant)
   #edge_arr = [topUp, topLeft, topRight, topDown, underUp, underLeft, underRight, underDown, frontLeft, rightLeft, leftLeft, backLeft]
   def __init__(self, corner_arr = corner_set, edge_arr = edge_set):
      self.corner_arr = corner_arr
      self.edge_arr = edge_arr
   
   #it would be cool if there was a better way to get the sides
   def get_up(self):
      top_row = [self.corner_arr[0].facing_color, self.edge_arr[0].color1, self.corner_arr[1].facing_color]
      mid_row = [self.edge_arr[1].color1, 'u', self.edge_arr[2].color1]
      bom_row = [self.corner_arr[2].facing_color, self.edge_arr[3].color1, self.corner_arr[3].facing_color]
      return [top_row, mid_row, bom_row]

   def get_down(self):
      top_row = [self.corner_arr[4].facing_color, self.edge_arr[4].color1, self.corner_arr[5].facing_color]
      mid_row = [self.edge_arr[5].color1, 'd', self.edge_arr[6].color1]
      bom_row = [self.corner_arr[6].facing_color, self.edge_arr[7].color1, self.corner_arr[7].facing_color]
      return [top_row, mid_row, bom_row]

   def get_front(self):
      top_row = [self.corner_arr[2].left_color, self.edge_arr[3].color2, self.corner_arr[3].up_color]
      mid_row = [self.edge_arr[8].color1, 'f', self.edge_arr[9].color2]
      bom_row = [self.corner_arr[4].up_color, self.edge_arr[4].color2, self.corner_arr[5].left_color]
      return [top_row, mid_row, bom_row]
   
   def get_back(self):
      top_row = [self.corner_arr[6].left_color, self.edge_arr[7].color2, self.corner_arr[7].up_color]
      mid_row = [self.edge_arr[10].color2, 'b', self.edge_arr[11].color1]
      bom_row = [self.corner_arr[0].up_color, self.edge_arr[0].color2, self.corner_arr[1].left_color]
      return [top_row, mid_row, bom_row]

   def get_left(self):
      top_row = [self.corner_arr[0].left_color, self.edge_arr[1].color2, self.corner_arr[2].up_color]
      mid_row = [self.edge_arr[10].color1, 'l', self.edge_arr[8].color2]
      bom_row = [self.corner_arr[6].up_color, self.edge_arr[5].color2, self.corner_arr[4].left_color]
      return [top_row, mid_row, bom_row]

   def get_right(self):
      top_row = [self.corner_arr[3].left_color, self.edge_arr[2].color2, self.corner_arr[1].up_color]
      mid_row = [self.edge_arr[9].color1, 'r', self.edge_arr[11].color2]
      bom_row = [self.corner_arr[5].up_color, self.edge_arr[6].color2, self.corner_arr[7].left_color]
      return [top_row, mid_row, bom_row]

   def display(self):
      u = self.get_up()
      f = self.get_front()
      d = self.get_down()
      b = self.get_back()
      l = self.get_left()
      r = self.get_right()

      #its like those paper cut out things that you turn into a box
      print()
      print('       {:s}'.format(' '.join(u[0])))
      print('       {:s}'.format(' '.join(u[1])))
      print('       {:s}'.format(' '.join(u[2])))
      print()
      print('{:s}  {:s}  {:s}'.format(' '.join(l[0]), ' '.join(f[0]), ' '.join(r[0])))
      print('{:s}  {:s}  {:s}'.format(' '.join(l[1]), ' '.join(f[1]), ' '.join(r[1])))
      print('{:s}  {:s}  {:s}'.format(' '.join(l[2]), ' '.join(f[2]), ' '.join(r[2])))
      print()
      print('       {:s}'.format(' '.join(d[0])))
      print('       {:s}'.format(' '.join(d[1])))
      print('       {:s}'.format(' '.join(d[2])))
      print()
      print('       {:s}'.format(' '.join(b[0])))
      print('       {:s}'.format(' '.join(b[1])))
      print('       {:s}'.format(' '.join(b[2])))
      print()
 
   def is_solved(self):
      #could also just compare given cube to solved cube ake Cube()
      #but that requires __eq__ method
      u = self.get_up()
      f = self.get_front()
      d = self.get_down()
      b = self.get_back()
      l = self.get_left()
      r = self.get_right()

      sides = [u, f, d, b, l, r]
      for side in sides:
            for row in side:
               if not(row[0] == row[1] == row[2]):
                  return False
      return True

   #probably don't have to build new arrays to do this
   def U(self):
      self.corner_arr = [self.corner_arr[2], self.corner_arr[0], self.corner_arr[3], self.corner_arr[1]] + self.corner_arr[4:]
      self.edge_arr = [self.edge_arr[1], self.edge_arr[3], self.edge_arr[0], self.edge_arr[2]] + self.edge_arr[4:]

   def D(self):
      self.corner_arr = self.corner_arr[:4] + [self.corner_arr[6], self.corner_arr[4], self.corner_arr[7], self.corner_arr[5]]
      self.edge_arr = self.edge_arr[:4] + [self.edge_arr[5], self.edge_arr[7], self.edge_arr[4], self.edge_arr[6]] + self.edge_arr[8:]

   #Everything after U and D is pretty gross
   def F(self):
      [c0, c1, c2, c3] = self.corner_arr[2:6]
      self.corner_arr = self.corner_arr[:2] + [Corner(True, c2.left_color, c2.up_color, c2.facing_color), 
                                               Corner(True, c0.up_color, c0.facing_color, c0.left_color),
                                               Corner(False, c3.up_color, c3.facing_color, c3.left_color),
                                               Corner(False, c1.left_color, c1.up_color, c1.facing_color)] + self.corner_arr[6:] 
      e0 = self.edge_arr[3]
      e1 = self.edge_arr[4]
      e2 = self.edge_arr[8]
      e3 = self.edge_arr[9]
      self.edge_arr = self.edge_arr[:3] + [Edge('top', e2.color2, e2.color1), e3] + self.edge_arr[5:8] + [Edge('mid', e1.color2, e1.color1), Edge('mid', e0.color1, e0.color2)] + self.edge_arr[10:]

   def B(self):
      [c0, c1] = self.corner_arr[:2]
      [c2, c3] = self.corner_arr[6:]
      self.corner_arr = [] + self.corner_arr[2:6] + []
      self.edge_arr = []

c = Cube()
for i in range(1000000):
   c.F()
c.display()
