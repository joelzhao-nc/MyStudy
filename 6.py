even = list(range(2, 11, 2))
print(even)


squares = []
for value in range(1, 11):
    square = value * 2
    squares.append(square)

print(squares)


sqs = [v**2 for v in range(1, 11)]
print(sqs)

for a in range(1, 21):
    print(a)

foods = ['a', 'b', 'c', 'd']
like_food = foods[:]

like_food = foods

print(like_food)
del foods[0]
print(like_food)
