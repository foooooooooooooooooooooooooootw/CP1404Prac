import random

print(random.randint(5, 20))  # line 1 smallest was 5, largest was 20
print(random.randrange(3, 10,
                       2))  # line 2 smallest was 3, largest was 9. Line 2 cannot produce a 4 because it only increases in steps of 2.
print(random.uniform(2.5, 5.5))  # line 3 smallest possible would be 2.5, largest I've seen was 5.253

print(random.randint(1, 100))
