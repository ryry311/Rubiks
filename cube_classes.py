#All pieces of a Rubiks cube are either a Corner(3 colors), an Edge(2 colors), or a Middle(1 color)
#Middles never move - white is always top, yellow bottom, orange/blue/red/green sides in that order
#Colors are one of: t(op), u(nder), f(ront)/green, (bac)k/blue, l(eft)/orange, r(ight)/red

class Corner:
   #There are 8 corners. a corner is either on the top side or the bottom side
   # "left" and "up" means if you orient the cube s.t. the piece is in the upper left corner
   def __init__(self, is_top, facing_color, left_color, up_color):
      self.is_top = is_top #bool
      self.facing_color = facing_color
      self.left_color = left_color
      self.up_color = up_color

class Edge:
   #12 edges. edges can be on top, bottom, or middle layer
   #if edge is on top or bottom, color1 is the facing color
   #otherwise, color1 is the counterclockwise color
   def __init__(self, layer, color1, color2):
      self.layer = layer
      self.color1 = color1
      self.color2 = color2

corner_set = [Corner(True, 't', 'l', 'b'),
              Corner(True, 't', 'b', 'r'),
              Corner(True, 't', 'f', 'l'),
              Corner(True, 't', 'r', 'f'),

              Corner(False, 'u', 'l', 'f'),
              Corner(False, 'u', 'f', 'r'),
              Corner(False, 'u', 'b', 'l'),
              Corner(False, 'u', 'r', 'b')]

edge_set = [Edge('top', 't', 'b'),
            Edge('top', 't', 'l'),
            Edge('top', 't', 'r'),
            Edge('top', 't', 'f'),
            
            Edge('bom', 'u', 'f'),  
            Edge('bom', 'u', 'l'),  
            Edge('bom', 'u', 'r'),  
            Edge('bom', 'u', 'b'),  

            Edge('mid', 'f', 'l'),
            Edge('mid', 'r', 'f'),
            Edge('mid', 'l', 'b'),
            Edge('mid', 'b', 'r')]

class Cube:
   #Position matters. corner_arr = [topQ2, topQ1, topQ3, topQ4, underQ2, underQ1, underQ3, underQ4] (Q meaning quadrant)
   #edge_arr = [topUp, topLeft, topRight, topDown, underUp, underLeft, underRight, underDown, frontLeft, rightLeft, leftLeft, backLeft]
   def __init__(self, corner_arr = corner_set, edge_arr = edge_set):
      self.corner_arr = corner_arr
      self.edge_arr = edge_arr

   def get_top(self):
      top_row = [self.corner_arr[0].facing_color, self.edge_arr[0].color1, self.corner_arr[1].facing_color]
      mid_row = [self.edge_arr[1].color1, 't', self.edge_arr[2].color1]
      bom_row = [self.corner_arr[2].facing_color, self.edge_arr[3].color1, self.corner_arr[3].facing_color]
      return [top_row, mid_row, bom_row]

   def get_under(self):
      top_row = [self.corner_arr[4].facing_color, self.edge_arr[4].color1, self.corner_arr[5].facing_color]
      mid_row = [self.edge_arr[5].color1, 'u', self.edge_arr[6].color1]
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
      t = self.get_top()
      f = self.get_front()
      u = self.get_under()
      b = self.get_back()
      l = self.get_left()
      r = self.get_right()

      print()
      print('       {:s}'.format(' '.join(t[0])))
      print('       {:s}'.format(' '.join(t[1])))
      print('       {:s}'.format(' '.join(t[2])))
      print()
      print('{:s}  {:s}  {:s}'.format(' '.join(l[0]), ' '.join(f[0]), ' '.join(r[0])))
      print('{:s}  {:s}  {:s}'.format(' '.join(l[1]), ' '.join(f[1]), ' '.join(r[1])))
      print('{:s}  {:s}  {:s}'.format(' '.join(l[2]), ' '.join(f[2]), ' '.join(r[2])))
      print()
      print('       {:s}'.format(' '.join(u[0])))
      print('       {:s}'.format(' '.join(u[1])))
      print('       {:s}'.format(' '.join(u[2])))
      print()
      print('       {:s}'.format(' '.join(b[0])))
      print('       {:s}'.format(' '.join(b[1])))
      print('       {:s}'.format(' '.join(b[2])))
      print()
 
   def clockwise_top(self):
      self.corner_arr = [self.corner_arr[2], self.corner_arr[0], self.corner_arr[3], self.corner_arr[1]] + self.corner_arr[4:]
      self.edge_arr = [self.edge_arr[1], self.edge_arr[3], self.edge_arr[0], self.edge_arr[2]] + self.edge_arr[4:]

c1 = Cube()
#c1.clockwise_top()
#c1.display()
