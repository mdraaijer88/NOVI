
def input_user():
    name = input("Wat is je naam? ")
    destination = input("Waar wil je naartoe? ")
    return f"{name}, en je wilt naar: {destination}"

def price():
    kilometer = int(input("Hoeveel kilometer? "))
    kosten = 0.40
    return kilometer * kosten

def main():
    user = input_user()
    kosten = price()
    print(user)
    print(f"Dat kost €{kosten:.2f}")

main()
main()
main()

