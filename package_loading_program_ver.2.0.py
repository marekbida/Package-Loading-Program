#pierwszy input usera.
num_items = int(input("Enter the number of items to be sent: ")) # int w tej lini wymusza na programie zeby wprowadzona wartoc potraktowal jako kliczbe calkowita.

# zmienne (var) dla info o paczkach.
packages = [] # [] oznacza liste ktora jest pusta w poczatkowej formie. Lista ta bedzie sie zmieniac podczas egzekucji programu.
current_package = [] #jak powyzej 
total_weight = 0 #tutaj jest 0 jako poczatkowa wartosc ale user bedzie mial mozliwosc wprowadzania roznych wartosci podczas wykonywania programu.
max_package_capacity = 20 #ta wartosc sie nie zmieni, bo to jest maksymalna akceptowalna waga paczki

# Wczytywanie i dodawanie przedmiotów do paczek
for item_number in range(1, num_items + 1): #poczatek petli gdzie "item_number" to nowa zmienna ktora bedzie przechowywac nowe wartosci. Funkcja Range bedzie zaczynala "liczyc" od 1 do "num_items" a potem doda 1. "num_items" jest zmienna ktora wprowadza user na poczatku wykonywania kodu.  
    while True:
        weight_input = input(f"Enter the weight of item {item_number} (1kg to max 10kg) (0 to exit): ")

        # Sprawdzenie czy wprowadzona wartość jest liczbą
        if weight_input.isdigit():
            weight = int(weight_input)
            # Sprawdzenie czy waga mieści się w przedziale 1-10 kg
            if 1 <= weight <= 10:
                # Sprawdzenie czy dodanie wagi nie przekroczy pojemności paczki
                if total_weight + weight > max_package_capacity:
                    # Jeśli tak, dodanie aktualnej paczki do listy paczek
                    packages.append(current_package)
                    # Przełączenie na nową paczkę
                    current_package = []
                    total_weight = 0
                # Dodanie wagi do bieżącej paczki
                current_package.append(weight)
                total_weight += weight
                # Sprawdzenie czy to ostatni przedmiot i czy paczka nie jest pełna
                if item_number == num_items or total_weight == max_package_capacity:
                    # Wysłanie paczki
                    packages.append(current_package)
                    current_package = []
                    total_weight = 0
                break
            else:
                # Komunikat o błędnej wadze
                print("Error: Weight must be between 1 and 10 kg.")
        elif weight_input == '0':
            # Zakończenie programu
            print("Exiting the program...")
            exit()
        else:
            # Komunikat o nieprawidłowej wartości
            print("Error: Please enter a valid weight.")

# Wyliczenie paczki z największym wolnym miejscem
# max_empty_space = max_package_capacity - max(max(sum(package) for package in packages), default=0)
max_empty_space = max(max_package_capacity - sum(package) for package in packages)
# Wyświetlenie informacji o paczkach
print("Number of sent packages:", len(packages))
print("Weight of sent packages:", [sum(package) for package in packages])
print("Leftover weight:", max_package_capacity * len(packages) - sum(sum(package) for package in packages))
print("Package with the most empty space:", max_empty_space) #sprawdzic czy wynik daje poprawna wartosc.
