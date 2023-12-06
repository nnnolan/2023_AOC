import math

with open("/Users/nolanpestano/Documents/GitHub/2023_AOC/6_day/input.txt") as file:
    data = file.read().splitlines()

def findWays(time, dist):
    count = 0
    for j in range(1, time):
        total_dist = (time - j) * j
        if total_dist >= dist:
            count += 1
    return count

times = [int(t) for t in data[0].split()[1:]]
dists = [int(d) for d in data[1].split()[1:]]
ways = []

for i in range(len(times)):
    ways.append(findWays(times[i], dists[i]))

time = int(data[0].split(":")[1].replace(" ", ""))
dist = int(data[1].split(":")[1].replace(" ", ""))

part1 = math.prod(ways)
part2 = findWays(time, dist)

print(part1, part2)