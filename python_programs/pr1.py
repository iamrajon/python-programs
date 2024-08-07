import random


names = ['Baverly', 'Hailee', 'Summer', 'Reshma', 'Gwen']

def findgf(boy):
    gf = random.choice(names)
    print(f"Dear {boy} your gf is: {gf}")


if __name__ == "__main__":
    boy = input("Enter Your name: ")
    findgf(boy)


