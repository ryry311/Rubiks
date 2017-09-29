class Corner:
	def __init__(self, facing_color, left_color, up_color):
		self.facing_color = facing_color
		self.left_color = left_color
		self.up_color = up_color
	def __eq__(self, other):
		return type(self) == type(other) and self.facing_color == other.facing_color and self.left_color == other.left_color and self.up_color == other.up_color
	def __repr__(self):
		return 'Corner({}, {}, {})'.format(self.facing_color, self.left_color, self.up_color)

class Edge:
	def __init__(self, color1, color2):
		self.color1 = color1
		self.color2 = color2
	def __eq__(self, other):
		return type(self) == type(other) and self.color1 == other.color1 and self.color2 == other.color2
	def __repr__(self):
		return 'Edge({}, {})'.format(self.color1, self.color2)

corner_set = [Corner('u', 'l', 'b'),
              Corner('u', 'b', 'r'),
              Corner('u', 'f', 'l'),
              Corner('u', 'r', 'f'),

              Corner('d', 'l', 'f'),
              Corner('d', 'f', 'r'),
              Corner('d', 'b', 'l'),
              Corner('d', 'r', 'b')]

edge_set = [Edge('u', 'b'),
            Edge('u', 'l'),
            Edge('u', 'r'),
            Edge('u', 'f'),
            
            Edge('d', 'f'),  
            Edge('d', 'l'),  
            Edge('d', 'r'),  
            Edge('d', 'b'), 

            Edge('f', 'l'),
            Edge('r', 'f'),
            Edge('l', 'b'),
            Edge('b', 'r')]

soln_cset = [Corner('u', 'l', 'b'),
              Corner('u', 'b', 'r'),
              Corner('u', 'f', 'l'),
              Corner('u', 'r', 'f'),

              Corner('d', 'l', 'f'),
              Corner('d', 'f', 'r'),
              Corner('d', 'b', 'l'),
              Corner('d', 'r', 'b')]

soln_eset = [Edge('u', 'b'),
              Edge('u', 'l'),
              Edge('u', 'r'),
              Edge('u', 'f'),
            
              Edge('d', 'f'),  
              Edge('d', 'l'),  
              Edge('d', 'r'),  
              Edge('d', 'b'), 

              Edge('f', 'l'),
              Edge('r', 'f'),
              Edge('l', 'b'),
              Edge('b', 'r')]

class Cube:
   def __init__(self, corner_arr = corner_set, edge_arr = edge_set):
      self.corner_arr = corner_arr
      self.edge_arr = edge_arr

   def __eq__(self, other):
      return type(self) == type(other) and self.corner_arr == other.corner_arr and self.edge_arr == other.edge_arr
   
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
      return self == Cube(soln_cset, soln_eset)
   
   def U(self):
      self.corner_arr[:4] = [self.corner_arr[2], self.corner_arr[0], self.corner_arr[3], self.corner_arr[1]]
      self.edge_arr[:4] = [self.edge_arr[1], self.edge_arr[3], self.edge_arr[0], self.edge_arr[2]]

   def D(self):
      self.corner_arr[4:] = [self.corner_arr[6], self.corner_arr[4], self.corner_arr[7], self.corner_arr[5]]
      self.edge_arr[4:8] = [self.edge_arr[5], self.edge_arr[7], self.edge_arr[4], self.edge_arr[6]]

   def F(self):
      [c0, c1, c2, c3] = self.corner_arr[2:6]
      self.corner_arr[2:6] = [Corner(c2.left_color, c2.up_color, c2.facing_color), Corner(c0.up_color, c0.facing_color, c0.left_color), Corner(c3.up_color, c3.facing_color, c3.left_color), Corner(c1.left_color, c1.up_color, c1.facing_color)]

      [e0, e1, e2, e3] = self.edge_arr[3:5] + self.edge_arr[8:10]
      self.edge_arr[3:5] = [Edge(e2.color2, e2.color1), e3]
      self.edge_arr[8:10] = [Edge(e1.color2, e1.color1), Edge(e0.color1, e0.color2)]
