# vars() function in Python

# vars(object)

class Geeks:
  def __init__(self, name1 = "Arun", num2 = 46, name3 = "Rishab"):
    self.name1 = name1
    self.num2 = num2
    self.name3 = name3
    
GeeksforGeeks = Geeks()
print(vars(GeeksforGeeks))