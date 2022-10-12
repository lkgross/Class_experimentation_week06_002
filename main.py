mountains = ['Mount Kilimanjaro', 'Mount Kenya', 'Mount Stanley', 'Mount Meru']
heights = [5895, 5199, 5109, 4562]
facts = []
for i in range(len(mountains)):
    facts.append(f'The height of {mountains[i]} is {heights[i]} m.')
print(facts)

mountains[3] = 'Mount Speke'
print(mountains)
print(heights)
print(min(heights))
print(max(heights))
# The total height is not meaningful.
print(sum(heights))

print(round(3.14159, 3))

print()

for height in heights:
    print(height)

print()

for i in range(len(heights)):
    print(heights[i])

print()

print(5 > 3)
print(heights[0] > 4562)

print()

print(type(5.3))
print(type(3))
print(type('Joey'))

# In computer science True and False are "boolean values",
# known to Python as "bool".
print(type(5 > 3))

print(f"Is 3 > 3? {3 > 3}")
print(f"Is 3 = 3? {3 == 3}")
print(f"Is 3 >= 3? {3 >= 3}")

print(type(True))
print(type('True'))
# Python looks for a variable called TRUE.
# It doesn't find f value for a variable TRUE.
# print(type(TRUE))

print(f"Does 3 not equal 3? {3 != 3}")

print(heights)
print()

print("Checking whether the mountains are higher than 4562 m.")
for height in heights:
    print("Checking mountain:")
    print(height > 4562)
print("We checked all the mountains.")

print()

# if 5895 > 4562:
#   print(f"The mountain is higher than 4562 m.")

if 4562 > 4562:
    print(f"The mountain is higher than 4562 m.")

print()

print("Checking whether the mountains are higher than 4562 m.")
for i in range(len(heights)):
    if heights[i] > 4562:
        print(f"{mountains[i]} is higher than 4562 m.")
print("We checked all the mountains.")

print()





