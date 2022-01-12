from math import *
from random import *

""" 
abs(-5) = 5
pow(4,2) = 4^2
max(5,12) = 12
min(5,12) = 5
round(3.44) = 3
round(3.99) = 4
floor(4.99) = 4
ceil(3.01) = 4
sqrt(16) = 4
sqrt(9) = 3
int(random() * 45 + 1) = 1~45
int(random()*45) = 0~44
randint(1,45) = 1~45
"""

off_study = int(randint(4,28))
print("The offline study date is " + str(off_study))

self_introduction = "KGH,2001.09.25,Man"
print("name = "+self_introduction[0:3] + ", Birth year = " + self_introduction[4:8] + ",  Birthday = " +  self_introduction[9:14] + ", Gender = " + self_introduction[15:])

test = "PyThOn"
test1 = "AbcabcAAAbccbCBAAaaACBc"
print(test.upper())
print(test.lower())
print(test[0].isupper()) 
#[print(test[A].isupper())] Make sure the A th digit is capital letter.
print(len(test))
print(test.replace("Py", "pY"))
print(test.index("T")) #[print(test.index("A""))] If there is no A, return the error.
print(test.find("t")) #[print(test.find("A"))] If there is no A, return -1.

index = test1.find("A")
print(index)
i = 0
while index != -1 :
  i = i + 1
  index = test1.find("A", + i)
  print(i)
  