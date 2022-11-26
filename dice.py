from random import randint

class Die:
    def __init__(self, sides=10):
        self.sides = sides

    def roll_die (self):
        return randint(1, self.sides)

D6 = Die()

#create empty list
results = []

for roll_num in range(10):
    result = D6.roll_die()
    results.append(result)
print ("\n10 rolls of a 6 sided die")
print(results)

# Make a 6-sided die, and show the results of 10 rolls.
d10 = Die(10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("10 rolls of a 10-sided die:")
print(results)