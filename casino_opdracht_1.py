import random

# If Test mode gevonden met AI
TEST_MODE = True

REGIS_FEE = 25.00
GAMB_TAX = 18.50
TICKET = 2.50

#persoonlijke gegegevens
if TEST_MODE:
    first_name = "Maarten"
    sur_name = "Draaijer"
    birthdate = "01-01-2000"
    sex = "m"
else:
    first_name = input("Wat is uw voornaam? ")
    sur_name = input("Wat is uw achternaam? ")
    birthdate = input("Wat is uw geboorte datum? (dd-mm-yyyy) ")
    sex = input("Wat is uw geslacht? (m/v/x) ").lower()

birth_day, birth_month, birth_year = birthdate.split("-")
age = 2026 - int(birth_year)
name = first_name + " " + sur_name
salutation = ""
sex = sex.lower()
if sex == "m":
    salutation = "meneer"
elif sex == "v":
    salutation = "mevrouw"
elif sex == "x":
    salutation = ""
else:
        print('Maak een geldige keuze (m/v/x')
if age < 18:
    print(f"Beste {salutation} {name}, Je bent helaas te jong om gebruik te maken van deze applicatie.")
    print(f"Applicatie wordt gesloten.")
    exit(1)


#budget FIXME print functies uitbreiden
if TEST_MODE:
    start_budget = 100.00
else:
    start_budget = float(input("Wat is uw startbudget in €? "))

total_budget  = start_budget - REGIS_FEE - GAMB_TAX - TICKET
print(
    f"Casino de Gouden Driehoek\n"
    f"-----------------------------\n"
    f"Beste {salutation} {name},\n\n"
    f"{f'Start budget €{start_budget:.2f}\n' if total_budget <= 0 else ''}"
    f"Inschrijfkosten -€{REGIS_FEE:.2f}\n"
    f"Gok belasting -€{GAMB_TAX:.2f}\n"
    f"Dagticket -€{TICKET:.2f}\n\n"
    f"Totaal Saldo €{total_budget:.2f}\n"
    f"-----------------------------\n"
    f"{'Uw speelsaldo is onvoldoende' if total_budget <= 0 else 'Uw speelsaldo is voldoende'}")


print("\nKies één van de volgende opties:")
print("1. Rood")
print("2. Zwart")
print("3. Even")
print("4. Oneven")

while True:
    #chance = random Hoe krijg ik dit aan het werk?
    choice = (input("Maak je keuze: "))
    if choice == "0":
        print("Bedankt voor het spelen. ")
        break
    elif choice == "1":
        print("Je hebt Rood gekozen")
    elif choice == "2":
        print("Je hebt Zwart gekozen")
    elif choice == "3":
        print("Je hebt Even gekozen")
    elif choice == "4":
        print("Je hebt Oneven gekozen")
    else:
        print("Kies een juiste keuze ")
        continue

    bet = float(input("Wat is je inzet? "))
    if bet <= 0:
        print("Kies een geldig bedrag...")
        continue
    elif bet < total_budget:
        print(f"U heeft niet genoeg saldo, saldo is {total_budget}")
    else:
        print(f"€{bet:.2f} is je inzet!")

    spin = random.randint(0, 36)

    if spin % 2 == 0:
        odd_even = "even"
    else:
        odd_even = "oneven"

    if spin <= 18:
        if odd_even == "even":
            color = "zwart"
        else:
            color = "rood"
    else:
        if odd_even == "even":
            color = "rood"
        else:
            color = "zwart"


    print("De roulette draait...") #Aantal seconden laten spinnen.. ?
    print(f"De roulette komt uit op: ({spin}) {color}")

    win = False

    if choice == "1" and color == "rood":
        win = True
    elif choice == "2" and color == "zwart":
        win = True
    elif choice == "3" and odd_even == "even":
        win = True
    elif choice == "4" and odd_even == "oneven":
        win = True

    if win:
        total_budget += bet
        print(f"Gefeliciteerd! Je wint €{bet:.2f}!")
    elif bet < total_budget:
        print(f"U heeft niet genoeg saldo...want saldo is {total_budget}")
        break
    else:
        total_budget -= bet
        print(f"Helaas, je verliest je inzet van €{bet:.2f}.")

    print(f"Je saldo is nu: €{total_budget:.2f}")

    again = input("Wil je nog een keer spelen? (j/n) ").lower()
    if again == "n":
        print("Bedankt voor het spelen.")
        break



