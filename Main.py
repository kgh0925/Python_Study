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