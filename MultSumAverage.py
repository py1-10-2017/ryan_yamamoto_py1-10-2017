
part1 = []
for y in range(0, 1000):
    if (y % 2 !=0):
        part1.append(y)
print part1

part2 = []
for x in range(5, 1000000):
    if (x % 5 ==0):
        part2.append(x)
print part2

a = [1, 2, 5, 10, 255, 3]
print sum(a)
print sum(a)/len(a)
