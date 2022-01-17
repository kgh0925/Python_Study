"""
[day1]
from math import *
from random import *


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

[day2]

url = "http://youtube.com"
my_str = url.replace("http://", "")

my_str = my_str[:my_str.index(".")]
print(my_str)

word = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print(word)

subway = ["A","B","C","A","A"]
print(subway)
print(subway.index("A"))
print(subway[1])
print(subway.count("A"))
print(subway.pop())
print(subway)
print(subway.count("A"))
subway.sort()
print(subway)
subway.reverse()
print(subway)
subway.clear()
print(subway)

[day3]
import random
weather = "rain"

if weather == "rain" :
  print("A")
elif weather == "Snow" :
  print("B")
else :
  print("C")

we = int(input("˚C? :"))
if 30 <= we :
  print("So Hot")
elif 20 <= we < 30 :
  print("So So")
elif 10 <= we < 20 :
  print("nice")
else :
  print("cold")

i = 1
People = 0
for i in range(1,51):
  Time = random.randint(5,50)
  print("Person ", i , "[Driving time :" , Time , "]")
  if 5 <= Time <= 15 :
    People += 1
print("Number of passengers to pick up:", People)

[day4]
import sys
print("Python", "Java", file = sys.stdout)

scores = {"A" :0, "B":50, "C":100}
for subject, score in scores.items():
 print(subject, score)

print("{0: >10}".format(500))

tank_name = "Tank"
tank_hp = 150
tank_damage = 35

print("{0} Start".format(tank_name))

"""