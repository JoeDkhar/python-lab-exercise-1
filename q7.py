import math

def area(a, b, c):
  s = (a + b + c) / 2
  return math.sqrt( s * (s - a) * (s - b) * (s - c))

a1 = float(input("Enter side a of the first triangle: "))
b1 = float(input("Enter side b of the first triangle: "))
c1 = float(input("Enter side c of the first triangle: "))
area1 = area(a1, b1, c1)

a2 = float(input("Enter side a of the second triangle: "))
b2 = float(input("Enter side b of the second triangle: "))
c2 = float(input("Enter side c of the second triangle: "))
area2 = area(a2, b2, c2)

total = area1 + area2
print("Total area:", total)
print("First triangle:", area1 / total * 100, "%")
print("Second triangle:", area2 / total * 100, "%")
