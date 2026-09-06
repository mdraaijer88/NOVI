
#persoonlijke gegegevens
first_name = input("Wat is uw voornaam? ")
sur_name = input("Wat is uw achternaam? ")
name = first_name + " " + sur_name
birthdate = input("Wat is uw geboorte datum? (dd-mm-yyyy) ")
sex = input("Wat is uw geslacht? (m/v/x) ").lower()
aanhef = ""
if sex == "m":
    aanhef = "meneer"
    print(f"Welkom {aanhef} {name} bij Casino de Gouden Driehoek")
elif sex == "v":
    aanhef = "mevrouw"
    print(f"Welkom {aanhef} {name} bij Casino de Gouden Driehoek")
elif sex == "x":
    print(f"Welkom {name} bij Casino de Goudendriehoek")
else:
    print("Maak een geldige keuze (m/v/x")

#budget FIXME print functies uitbreiden
start_budget = float(input("Wat is uw startbudget in €? "))
inschrijfkosten = 25.00
gok_belasting = 18.50
ticket = 2.50
totaal_budget  = start_budget - inschrijfkosten - gok_belasting - ticket
if totaal_budget <= 0:
    print("Casino de Gouden Driehoek")
    print("-----------------------------")
    print(f"Beste {aanhef} {name},")
    print()
    print(f"Start budget €{start_budget}")
    print(f"Inschrijfkosten -€{inschrijfkosten}")
    print(f"Gok belasting -€{gok_belasting}")
    print(f"Dagticket -€{ticket}")
    print()
    print(f"Totaal Saldo €{totaal_budget}")
    print("-----------------------------")
    print("Uw speelsaldo is onvoldoende")
else:
    print("Casino de Gouden Driehoek")
    print("-----------------------------")
    print(f"Beste {aanhef} {name},")
    print()
    print(f"Inschrijfkosten -€{inschrijfkosten}")
    print(f"Gok belasting -€{gok_belasting}")
    print(f"Dagticket -€{ticket}")
    print(f"-----------------------------)")
    print(f"Het totaal budget is: €{totaal_budget}")