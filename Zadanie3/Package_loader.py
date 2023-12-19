
element = int(input('Enter the number of elements you wish to send: '))     #Pytanie o ilość elementów.

weights = 0                     #Waga paczek.
sum_weights = 0                 #Suma wag paczek.
total_sum_weights = 0           #Suma wag wszystkich paczek.
sent = 0                        #Ilość wysłanych paczek.

for package in range(element):
    weight = int(input('Enter the weight of the elements (between 1kg to 10kg): '))     #Pytanie o wagę każdej paczki.
    weights += weight
    sum_weights += weight
    total_sum_weights += weight
    print('The weight of Your packages: ', weights)

    if sum_weights >= 20:       #Warunek dla załadowanych elementów równych lub powyżej 20kg.
        sum_weights = 0
        sent += 1

    if package == (element - 1) and sum_weights > 0:        #Warunek sprawdza ilość wysłanych elementów w paczce i sumę wag.
        print("Last package. ")
        sent += 1

    if weights >= 1 and weights <= 10:      #Warunek sprawdza, czy waga elementu mieści sie między 1 i 10kg.
        print('The weight of your package is within the range.')

    if weight < 1 or weight > 10:       #Warunek sprawdza, czy waga elementu jest mniejsz niż 1kg i większa niż 10kg. Jeżeli tak to przerwij.
        print('Error, enter a value above size')
        break

    if sum_weights > 20:        #Warunek dla sumy wag elementów, jeżeli suma jest powyżej 20kg to przejdź dalej.
        pass

print("Number of kilograms shipped: ", total_sum_weights)
print("Number of packages shipped: ", sent)
print("Number of empty kilograms shipped: ", sent*20 - total_sum_weights)