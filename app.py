class Rectangle:
  width = 0
  height = 0

  def __init__(self, width, height):
    self.set_width(width)
    self.set_height(height)
  
  def __repr__(self):
    return "Rectangle(width={width}, height={height})".format(width=self.width, height=self.height)

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perimeter = (2 * self.width) + (2 * self.height)
    return perimeter

  def get_diagonal(self):
    diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
    return diagonal

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      widthStr = ''
      rowsList = []
      while len(widthStr) < self.width:
        widthStr = widthStr + "*"
      while len(rowsList) < self.height:
        rowsList.append(widthStr)
      output = "\n".join(rowsList)
      return output + "\n"
  
  def get_amount_inside(self, object):
    count = 0
    while self.height >= object.height:
      rowCount = self.width/object.width
      count = count + rowCount
      self.height = self.height - object.height
    return int(count)

  
class Square(Rectangle):
  def __init__(self, side):
    self.set_side(side)
  
  def __repr__(self):
    return "Square(side={side})".format(side=self.width)
  
  def set_side(self, side):
    self.set_width(side)
    self.set_height(side)

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))