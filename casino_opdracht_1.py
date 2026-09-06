# If Test mode wel gevonden via AI
TEST_MODE = True

REGIS_FEE = 25.00
GAMB_TAX = 18.50
TICKET = 2.50

#persoonlijke gegegevens
if TEST_MODE:
    first_name = "Jan"
    sur_name = "Jansen"
    birthdate = "01-01-2015"
    sex = "m"
else:
    first_name = input("Wat is uw voornaam? ")
    sur_name = input("Wat is uw achternaam? ")
    birthdate = input("Wat is uw geboorte datum? (dd-mm-yyyy) ")

birth_day, birth_month, birth_year = birthdate.split("-")
age = 2026 - int(birth_year)

name = first_name + " " + sur_name
sex = sex.lower()

salutation = ""
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
    exit(1)


#budget FIXME print functies uitbreiden
if TEST_MODE:
    start_budget = 100.00
else:
    start_budget = float(input("Wat is uw startbudget in €? "))

total_budget  = start_budget - REGIS_FEE - GAMB_TAX - TICKET
if total_budget <= 0:
    print("Casino de Gouden Driehoek")
    print("-----------------------------")
    print(f"Beste {salutation} {name},")
    print()
    print(f"Start budget €{start_budget:.2f}")
    print(f"Inschrijfkosten -€{REGIS_FEE:.2f}")
    print(f"Gok belasting -€{GAMB_TAX:.2f}")
    print(f"Dagticket -€{TICKET:.2f}")
    print()
    print(f"Totaal Saldo €{total_budget:.2f}")
    print("-----------------------------")
    print("Uw speelsaldo is onvoldoende")
else:
    print("Casino de Gouden Driehoek")
    print("-----------------------------")
    print(f"Beste {salutation} {name},")
    print()
    print(f"Inschrijfkosten -€{REGIS_FEE:.2f}")
    print(f"Gok belasting -€{GAMB_TAX:.2f}")
    print(f"Dagticket -€{TICKET:.2f}")
    print(f"-----------------------------)")
    print(f"Het totaal budget is: €{total_budget:.2f}")