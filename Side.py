class Side:
   def __init__(self, color):
      self.color = color
      self.row1 = [color, color, color]
      self.row2 = [color, color, color]
      self.row3 = [color, color, color]
      self.col1 = [color, color, color]
      self.col3 = [color, color, color]

   def __eq__(self, other):
      return type(self) == type(other) and self.color == other.color and self.row1 == other.row1 and self.row3 == other.row3 and self.col1[1] == other.col1[1] and self.col3[1] == other.col3[1]

   def __repr__(self):
      return " {} {} {}\n {} {} {}\n {} {} {}".format(self.row1[0], self.row1[1], self.row1[2], self.col1[1], self.color, self.col3[1], self.row3[0], self.row3[1], self.row3[2])

   def refresh_rows(self):
      self.row1[0] = self.col1[0]
      self.row1[2] = self.col3[0]
      self.row2[0] = self.col1[1]
      self.row2[2] = self.col3[1]
      self.row3[0] = self.col1[2]
      self.row3[2] = self.col3[2]
      
   def refresh_cols(self):
      self.col1[0] = self.row1[0]
      self.col1[2] = self.row3[0]
      self.col3[0] = self.row1[2]
      self.col3[2] = self.row3[2]

   def cost(self):
      cost = 0
      for tile in self.row1:
         if tile != self.color:
            cost += 1
      for tile in self.row3:
         if tile != self.color:
            cost += 1
      if self.col1[1] != self.color:
         cost += 1
      if self.col3[1] != self.color:
         cost += 1
      return cost

   def rotate_clockwise(self):
      reverse2(self.col1, self.col3)
      self.row2[0] = self.row3[1]
      self.row2[2] = self.row1[1]
      self.row1, self.col1, self.row3, self.col3 = self.col1, self.row3, self.col3, self.row1

   def rotate_counter_clockwise(self):
      reverse2(self.row1, self.row3)
      self.row2[2] = self.row3[1]
      self.row2[0] = self.row1[1]
      self.col1, self.row3, self.col3, self.row1 = self.row1, self.col1, self.row3, self.col3

def reverse2(arr1, arr2):
   arr1[0], arr1[2], arr2[0], arr2[2] = arr1[2], arr1[0], arr2[2], arr2[0] 
