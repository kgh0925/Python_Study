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