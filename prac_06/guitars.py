from prac_06.guitar import Guitar

guitars = []

print("My guitars!")

name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(guitar, "added.")
    name = input("Name: ")

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (Vintage)" if guitar.is_vintage() else ""
    print("Guitar {}: {:} ({}), worth ${:10,.2f}{}".format(i, guitar.name, guitar.year, guitar.cost,
                                                           vintage_string))
