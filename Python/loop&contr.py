#Loop Control statement

fruits = ["apple", "banana", "grape", "date"]

for fruit in fruits:
    if fruit == "grape":
     break # Exits the loop if grape is found
print(fruit)

print()
for fruit in fruits:
    if fruit == "grape":
     continue # Skips grape and moves to the iteration
print(fruit)
