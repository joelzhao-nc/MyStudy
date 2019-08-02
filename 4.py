motorcycles = ['a', 'b', 'c']

print(motorcycles)
print(motorcycles[0])
motorcycles.append('d')

print(motorcycles)
motorcycles.insert(0, 'z')
del motorcycles[4]
print(motorcycles)

i = 1

del motorcycles[i]

print(motorcycles)

last = motorcycles.pop(1)

print(last)
print(motorcycles)

for motor in motorcycles:
    print(motor)
