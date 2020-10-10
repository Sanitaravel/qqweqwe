a = (input())

first_half = 0
second_half = 0

for i in range(3):
    first_half += int(a[i])

for i in range (3, 6):
    second_half += int(a[i])

if first_half == second_half:
    print("This is lucky ticket!")
else:
    print("This isn't lucky ticket!")