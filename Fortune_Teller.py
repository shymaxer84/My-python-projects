import datetime
import random

today = datetime.date.today()

year = int(today.strftime("%Y"))

Person_name = input("Enter your name")
Person_age = int(input("Enter your year of birth"))

Person_Age = year - Person_age

fortunes = [
    "You will find love in unexpected places.",
    "A financial windfall is in your future.",
    "Your dreams will come true if you have the courage to pursue them.",
    "The stars are aligned in your favor.",
    "You will soon embark on a great adventure.",
    "Good things come to those who wait.",
    "You will meet a stranger who will change your life.",
    "You will travel to a new place and discover something amazing.",
    "Your hard work will pay off and bring you success.",
    "Someone special will come into your life soon.",
    "A great opportunity is headed your way - be ready to seize it.",
    "You will overcome a challenge and emerge stronger than before.",
    "Your creativity and passion will lead you to great accomplishments.",
    "Your kindness and generosity will be rewarded in unexpected ways.",
    "You will make a new friend who will become an important part of your life.",
    "A major change is coming, but it will ultimately be for the better.",
    "You will receive unexpected help from someone when you need it most."
]

fortuneIndex = random.choice(fortunes)
print("Hello", Person_name, "You are", Person_Age, "year old,\n")
print("Your fortune is:!", fortuneIndex, "\n")

while True:

    answer = input("Would you like another fortune? (Y/N)")

    if answer in ('n', 'N'):
        break

    fortuneIndex = random.choice(fortunes)
    print("Your new fortune is:", fortuneIndex, "\n")

print("Thank you for using the Fortune Teller")
