#cubes = []
#
#for number in range(1, 11):
#    cubes.append(number ** 3)
#
#for cube in cubes:
#    print(cube)

cubes = [number ** 3 for number in range(1, 11)]

for cube in cubes:
    print(cube)