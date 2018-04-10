from Side import Side, reverse2

class Cube:
   def __init__(self, front, right, up, left, back, down):
      self.front = front
      self.right = right
      self.up = up
      self.left = left
      self.back = back
      self.down = down
      self.side_arr = [self.front, self.right, self.up, self.left, self.back, self.down]

   def __eq__(self, other):
      return type(self) == type(other) and self.front == other.front and self.right == other.right and self.up == other.up and self.left == other.left and self.back == other.back and self.down == other.down

   def __repr__(self):
      return "up:\n{}\n\nleft:\n{}\nfront:\n{}\nright:\n{}\nback:\n{}\n\ndown:\n{}\n".format(self.up, self.left, self.front, self.right, self.back, self.down)

   def print_cube(self):
      print("\n         {}".format(' '.join(self.up.row1)))
      print("         {}".format(' '.join(self.up.row2)))
      print("         {}\n".format(' '.join(self.up.row3)))

      print("  {}  {}  {}  {}".format(' '.join(self.left.row1), ' '.join(self.front.row1), ' '.join(self.right.row1), ' '.join(self.back.row1)))
      print("  {}  {}  {}  {}".format(' '.join(self.left.row2), ' '.join(self.front.row2), ' '.join(self.right.row2), ' '.join(self.back.row2)))
      print("  {}  {}  {}  {}\n".format(' '.join(self.left.row3), ' '.join(self.front.row3), ' '.join(self.right.row3), ' '.join(self.back.row3)))

      print("         {}".format(' '.join(self.down.row1)))
      print("         {}".format(' '.join(self.down.row2)))
      print("         {}\n".format(' '.join(self.down.row3)))

   def cost(self):
      cost = 0
      for side in self.side_arr:
         cost += side.cost()
      return cost

   def view_change_left(self):
      self.front, self.right, self.back, self.left = self.right, self.back, self.left, self.front
      self.up.rotate_clockwise()
      self.down.rotate_counter_clockwise()
   
   def view_change_right(self):
      self.right, self.back, self.left, self.front = self.front, self.right, self.back, self.left 
      self.down.rotate_clockwise()
      self.up.rotate_counter_clockwise()

   def view_change_up(self):
      self.back.rotate_clockwise()
      self.back.rotate_clockwise()
      self.up.rotate_clockwise()
      self.up.rotate_clockwise()
      self.up, self.front, self.down, self.back = self.front, self.down, self.back, self.up

      self.right.rotate_clockwise()
      self.left.rotate_counter_clockwise()
   
   def view_change_down(self):
      self.back.rotate_clockwise()
      self.back.rotate_clockwise()
      self.down.rotate_clockwise()
      self.down.rotate_clockwise()

      self.front, self.down, self.back, self.up = self.up, self.front, self.down, self.back

      self.left.rotate_clockwise()
      self.right.rotate_counter_clockwise()

   def U(self):
      self.up.rotate_clockwise()

      self.left.row1, self.front.row1, self.right.row1, self.back.row1 = self.front.row1, self.right.row1, self.back.row1, self.left.row1

      self.left.refresh_cols()
      self.front.refresh_cols()
      self.right.refresh_cols()
      self.back.refresh_cols()
   
   def Ui(self):
      self.up.rotate_counter_clockwise()

      self.front.row1, self.left.row1, self.back.row1, self.right.row1 = self.left.row1, self.back.row1, self.right.row1, self.front.row1
   
      self.left.refresh_cols()
      self.front.refresh_cols()
      self.right.refresh_cols()
      self.back.refresh_cols()
   
   def D(self):
      self.down.rotate_clockwise()

      self.front.row3, self.left.row3, self.back.row3, self.right.row3 = self.left.row3, self.back.row3, self.right.row3, self.front.row3 

      self.left.refresh_cols()
      self.front.refresh_cols()
      self.right.refresh_cols()
      self.back.refresh_cols()
   
   def Di(self):
      self.down.rotate_counter_clockwise()
      
      self.left.row3, self.front.row3, self.right.row3, self.back.row3 = self.front.row3, self.right.row3, self.back.row3, self.left.row3

      self.left.refresh_cols()
      self.front.refresh_cols()
      self.right.refresh_cols()
      self.back.refresh_cols()

   def R(self):
      self.right.rotate_clockwise()
      reverse2(self.back.col1, self.down.col3)

      self.up.col3, self.front.col3, self.down.col3, self.back.col1 = self.front.col3, self.down.col3, self.back.col1, self.up.col3

      self.up.refresh_rows()
      self.front.refresh_rows()
      self.down.refresh_rows()
      self.back.refresh_rows()
   
   def Ri(self):
      self.right.rotate_counter_clockwise()
      reverse2(self.back.col1, self.down.col3)

      self.up.col3, self.back.col1, self.down.col3, self.front.col3 = self.back.col1, self.down.col3, self.front.col3, self.up.col3

      self.up.refresh_rows()
      self.front.refresh_rows()
      self.down.refresh_rows()
      self.back.refresh_rows()
   
   def L(self):
      self.left.rotate_clockwise()      
      reverse2(self.back.col3, self.down.col1)
      
      self.up.col1, self.back.col3, self.down.col1, self.front.col1 = self.back.col3, self.down.col1, self.front.col1, self.up.col1 

      self.up.refresh_rows()
      self.front.refresh_rows()
      self.down.refresh_rows()
      self.back.refresh_rows()

   def Li(self):
      self.left.rotate_counter_clockwise()
      reverse2(self.back.col3, self.down.col1)
      
      self.up.col1, self.front.col1, self.down.col1, self.back.col3 = self.front.col1, self.down.col1, self.back.col3, self.up.col1 

      self.up.refresh_rows()
      self.front.refresh_rows()
      self.down.refresh_rows()
      self.back.refresh_rows()
  
   def F(self):
      self.front.rotate_clockwise() 
      reverse2(self.left.col3, self.right.col1)

      self.up.row3, self.left.col3, self.down.row1, self.right.col1 = self.left.col3, self.down.row1, self.right.col1, self.up.row3

      self.right.refresh_rows()
      self.left.refresh_rows()
      self.up.refresh_cols()
      self.down.refresh_cols()
   
   def Fi(self):
      self.front.rotate_counter_clockwise()  
      reverse2(self.left.col3, self.right.col1)

      self.up.row3, self.right.col1, self.down.row1, self.left.col3 = self.right.col1, self.down.row1, self.left.col3, self.up.row3

      self.right.refresh_rows()
      self.left.refresh_rows()
      self.up.refresh_cols()
      self.down.refresh_cols()
      
   def B(self):
      self.back.rotate_clockwise()  
      reverse2(self.left.col1, self.right.col3)

      self.up.row1, self.right.col3, self.down.row3, self.left.col1 = self.right.col3, self.down.row3, self.left.col1, self.up.row1, 

      self.right.refresh_rows()
      self.left.refresh_rows()
      self.up.refresh_cols()
      self.down.refresh_cols()

   def Bi(self):
      self.back.rotate_counter_clockwise() 
      reverse2(self.left.col1, self.right.col3)

      self.up.row1, self.left.col1, self.down.row3, self.right.col3 = self.left.col1, self.down.row3, self.right.col3, self.up.row1 

      self.right.refresh_rows()
      self.left.refresh_rows()
      self.up.refresh_cols()
      self.down.refresh_cols()
