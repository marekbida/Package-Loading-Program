num_items = int(input("Enter the number of items to be sent: ")) # int w tej lini wymusza na programie zeby wprowadzona wartoc potraktowal jako kliczbe calkowita.
package_weight = 0
total_weight = 0
num_of_packages = 0
max_unused_kg = 0
package_number_that_had_the_most_unused_capacity = 0

for item in range (num_items):
    item_weight = int(input ("podaj wage przedmiotu (1kg - 10kg): "))
    if item_weight < 1 or item_weight > 10:
        print("Waga jest nie prawidlowa")
        break
    package_weight += item_weight
    if package_weight > 20:
        package_weight -= item_weight
        total_weight += package_weight
        num_of_packages += 1
        print(f"Wysylamy paczke nr {num_of_packages} o wadze {package_weight} kg")
        if 20 - package_weight > max_unused_kg:
            max_unused_kg = 20 - package_weight
            package_number_that_had_the_most_unused_capacity = num_of_packages
        package_weight = item_weight
    elif package_weight == 20:
        total_weight += package_weight
        num_of_packages += 1
        print(f"Wysylamy paczke nr {num_of_packages} o wadze {package_weight} kg")
        package_weight = 0
if package_weight > 0:
    total_weight += package_weight
    num_of_packages += 1
    if 20 - package_weight > max_unused_kg:
        max_unused_kg = 20 - package_weight
        package_number_that_had_the_most_unused_capacity = num_of_packages
    print(f"Wysylamy paczke nr {num_of_packages} o wadze {package_weight} kg")
unused_weight = num_of_packages * 20 - total_weight

print(f"Nie wykorzystana waga to {unused_weight} kg.")

print(f"w sumie wyslalismy {total_weight} kg")
print(f"W sumie wyslalismy {num_of_packages} paczek.")
print(f"Paczka nr {package_number_that_had_the_most_unused_capacity} miala {max_unused_kg} nie wykorzystanej wagi")




wojciech.niekrasz@gmail.com





