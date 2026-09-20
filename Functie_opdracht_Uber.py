def type_uber():
    print("Welke Uber kies je:")
    print("1. Uber Black")
    print("2. Uber Van")
    print("3. Uber X")


def user_choice(choice):
    if choice == 1:
        return "Uber Black"
    elif choice == 2:
        return "Uber Van"
    elif choice == 3:
        return "Uber X"
    else:
        return "onbekend"


def get_price_km(choice):
    if choice == 1:
        return 2.00
    elif choice == 2:
        return 3.50
    elif choice == 3:
        return 1.50
    else:
        return 0


def bereken_kosten(price_km, distance):
    return price_km * distance


type_uber()

choice = int(input("Je keuze: "))
name = user_choice(choice)
price_km = get_price_km(choice)

distance = float(input("Afstand in km: "))
kosten = bereken_kosten(price_km, distance)

print("Je koos", name)
print("De rit kost", kosten, "euro")