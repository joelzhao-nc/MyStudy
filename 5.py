a = ['a1', 'a2', 'a3', 'a4']
b = ['b1', 'b2', 'b3', 'b4']
c = ['c1', 'c2', 'c3', 'c4']
d = ['d1', 'd2', 'd3', 'd4']

magics = [a, b, c, d]

for magic in magics:
    print(magic)
    for mag in magic:
        print(mag)
print("end")
