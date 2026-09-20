from datetime import date
import random

REGIS_FEE = 25.00
GAMB_TAX = 18.50
TICKET = 2.50


def user_input():
    first_name = input("Wat is uw voornaam? ")
    sur_name = input("Wat is uw achternaam? ")
    birthdate = input("Wat is uw geboortedatum? (dd-mm-yyyy) ")
    gender = input("Wat is uw geslacht? (m/v/x) ").lower()
    # TODO: controleren of gender m, v of x is
    # TODO: controleren of birthdate echt dd-mm-yyyy is
    return first_name, sur_name, birthdate, gender


def determine_salutation(sur_name, gender):
    if gender == "m":
        return "meneer " + sur_name
    elif gender == "v":
        return "mevrouw " + sur_name
    else:
        return sur_name


def check_age(birthdate):
    birth_day, birth_month, birth_year = birthdate.split("-")
    today = date.today()
    age = today.year - int(birth_year)
    if today.month < int(birth_month) or (today.month == int(birth_month) and today.day < int(birth_day)):
        age = age - 1
    return age


def define_start_budget():
    # TODO: try/except voor als iemand een letter typt
    start_budget = float(input("Wat is uw startbudget in €? "))
    total_budget = start_budget - REGIS_FEE - GAMB_TAX - TICKET
    return start_budget, total_budget


def show_welcome_message(start_budget, total_budget, salutation):
    print("Casino de Gouden Driehoek")
    print("-----------------------------")
    print(f"Beste {salutation},\n")
    print(f"Start budget     €{start_budget:.2f}")
    print(f"Inschrijfkosten -€{REGIS_FEE:.2f}")
    print(f"Gok belasting   -€{GAMB_TAX:.2f}")
    print(f"Dagticket       -€{TICKET:.2f}\n")
    print(f"Totaal saldo     €{total_budget:.2f}")
    print("-----------------------------")
    if total_budget <= 0:
        print("Uw speelsaldo is onvoldoende")
    else:
        print("Uw speelsaldo is voldoende")

def show_games_menu():
    print("\nKies een spel:")
    print("1. Roulette")
    print("2. Fruitmachine")
    print("0. Stoppen")

def roulette_spel(total_budget):
    print("\nKies één van de volgende opties:")
    print("1. Rood")
    print("2. Zwart")
    print("3. Even")
    print("4. Oneven")
    print("0. Stoppen")

    while True:
        choice = input("Maak je keuze: ")
        if choice == "0":
            print("Bedankt voor het spelen.")
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
            print("Kies een juiste keuze")
            continue

        # TODO: try/except voor als iemand een letter typt
        bet = float(input("Wat is je inzet? "))
        if bet <= 0:
            print("Kies een geldig bedrag...")
            continue
        elif bet > total_budget:
            print(f"U heeft niet genoeg saldo, saldo is €{total_budget:.2f}")
            continue
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

        print("De roulette draait...")
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
        else:
            total_budget -= bet
            print(f"Helaas, je verliest je inzet van €{bet:.2f}.")

        print(f"Je saldo is nu: €{total_budget:.2f}")

        if total_budget <= 0:
            print("Je saldo is op.")
            break

        again = input("Wil je nog een keer spelen? (j/n) ").lower()
        if again == "n":
            print("Bedankt voor het spelen.")
            break

    return total_budget



def main():
    first_name, sur_name, birthdate, gender = user_input()
    salutation = determine_salutation(sur_name, gender)
    age = check_age(birthdate)

    if age < 18:
        print(f"Beste {salutation}, je bent helaas te jong om gebruik te maken van deze applicatie.")
        print("Applicatie wordt gesloten.")
        return

    start_budget, total_budget = define_start_budget()
    show_welcome_message(start_budget, total_budget, salutation)
    show_games_menu()

    # TODO: hoofdmenu en fruitmachine
    while total_budget > 0:
        total_budget = roulette_spel(total_budget)

        if total_budget <= 0:
            break

        opnieuw = input("Wil je opnieuw naar de roulette? (j/n) ").lower()
        if opnieuw != "j":
            break

    print(f"Uw eindsaldo is €{total_budget:.2f}")


main()