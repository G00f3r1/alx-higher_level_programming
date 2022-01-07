
#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square

s1 = Square(3, 5, 1, 87)
s1_dictionary = s1.to_dictionary()

s2 = Square.create(**s1_dictionary)

print(str(s1))
print(str(s2))
print(s1_dictionary)
