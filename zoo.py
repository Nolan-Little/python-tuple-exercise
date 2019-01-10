# Create a tuple named zoo that contains your favorite animals.

# Find one of your animals using the .index(value) method on the tuple.

# Determine if an animal is in your tuple by using value in tuple.

# Create a variable for each of the animals in your tuple with this cool feature of Python.

# # example
# (lizard, fox, mammoth) = zoo
# print(lizard)
# Convert your tuple into a list.

# Use extend() to add three more animals to your zoo.

# Convert the list back into a tuple.

zoo = ('Kangaroo', 'Wombat', 'Emu', 'Seal', 'Otter', 'Lynx')

kangaroo, wombat, emu, seal, otter, lynx = zoo

print("line 22:", wombat)
zoo = list(zoo)

new_animals = ["Giraffe", "Elephant", "Polar Bear"]
zoo.extend(new_animals)

zoo = tuple(zoo)


def find_animal(animal):
    print("Find Animal index in zoo:")
    try:
        print(zoo.index(animal))
    except:
        print("That animal isn't in the zoo")

def find_animal_2(animal):
    if animal in zoo:
        print(f"{animal} is in the zoo")
    else:
        print(f"The zoo doesn't have any {animal}")

find_animal("Seal")
find_animal_2("Wombat")
print(zoo)

