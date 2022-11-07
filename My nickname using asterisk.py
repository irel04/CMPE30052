# CMPE30052 - Data Structures and Algorithms

print(f"\n{'=' * 75}")
print(f"{'|'}{' ': >5}{'Assignment 1 | Programmed by Irel Kian C. Bacolod'}{' ': >19}{'|'}")
print(f"{'=' * 75}")

# This is very lengthy program sir but this the only algorithm I can think of ^_^. Thank you !!!

print("\n")
# Row 1
for i in range(23):
    if i <= 4:
        print("*", end="")
    elif 4 < i <= 8:
        print(" ", end="")
    elif 8 < i <= 14:
        print("*", end="")
    elif 14 < i < 18:
        print(" ", end="")
    elif 18 == i:
        print("*")
        break

# Row 2
for i in range(23):
    if i == 0:
        print("*", end="")
    elif 0 < i < 5:
        print(" ", end="")
    elif i == 5:
        print("*", end="")
    elif 5 < i < 9:
        print(" ", end="")
    elif i == 9:
        print("*", end="")
    elif 9 < i < 18:
        print(" ", end="")
    elif i == 18:
        print("*")

# Row 3
for i in range(23):
    if i == 0:
        print("*", end="")
    elif 0 < i < 5:
        print(" ", end="")
    elif i == 5:
        print("*", end="")
    elif 5 < i < 9:
        print(" ", end="")
    elif i == 9:
        print("*", end="")
    elif 9 < i < 18:
        print(" ", end="")
    elif i == 18:
        print("*")
# Row 4
for i in range(23):
    if 0 <= i <=4:
        print("*", end="")
    elif 4 < i < 9:
        print(" ", end="")
    elif 9 <= i <= 14:
        print("*", end="")
    elif 14 < i < 18:
        print(" ", end="")
    elif 18 <= i <= 23:
        print("*")
        break

# Row 5
for i in range(23):
    if i == 0:
        print("*", end="")
    elif 0 < i < 2:
        print(" ", end="")
    elif i == 2:
        print("*", end="")
    elif 2 < i < 9:
        print(" ", end="")
    elif i == 9:
        print("*", end="")
    elif 9 < i < 18:
        print(" ", end="")
    elif i == 18:
        print("*")

# Row 6
for i in range(23):
    if i == 0:
        print("*", end="")
    elif 0 < i < 3:
        print(" ", end="")
    elif i == 3:
        print("*", end="")
    elif 3 < i < 9:
        print(" ", end="")
    elif i == 9:
        print("*", end="")
    elif 9 < i < 18:
        print(" ", end="")
    elif i == 18:
        print("*")
        break

# Row 7
for i in range(23):
    if i == 0:
        print("*", end="")
    elif 0 < i < 4:
        print(" ", end="")
    elif i == 4:
        print("*", end="")
    elif 4 < i < 9:
        print(" ", end="")
    elif 9 <= i <= 14:
        print("*", end="")
    elif 9 < i < 18:
        print(" ", end="")
    elif 18 <= i <= 23:
        print("*", end="")

print("\n")
