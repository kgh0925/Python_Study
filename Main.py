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
