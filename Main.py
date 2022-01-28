import turtle as t
t.speed("fastest")
color = ["Red","Purple","Blue","Yellow","Green","White"]
t.bgcolor("Black")
for i in range(1000):
  t.color(color[i%6])
  t.fd(i)
  t.left(91)
