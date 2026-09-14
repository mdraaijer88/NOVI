def input_user():
    name = input("Wat is je naam? ")
    destination = input("Waar wil je naartoe? ")
    return f"{name}, en je wilt naar: {destination}"

def price():
    kilometer = int(input("Hoeveel kilometer? "))
    kosten = 0.40
    return kilometer * kosten

print(input_user())
print(f"Dat kost €{price():.2f}")

print(input_user())
print(f"Dat kost €{price():.2f}")



